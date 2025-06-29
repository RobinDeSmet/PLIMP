import os
import google.generativeai as genai
from typing import Callable, List, Dict
from plimp.assistant.prompts import SYSTEM_PROMPT
from plimp.assistant.exceptions import AssistantConversationError
from plimp.utils.logger import logger


class GeminiAssistant:
    def __init__(
        self,
        api_key: str,
        model_name: str = "gemini-2.0-flash-exp",
        tools: List[Callable] = None,
        tools_mapping: Dict[str, Callable] = None,
    ):
        if not api_key:
            raise ValueError("Missing API key for Gemini Assistant.")

        genai.configure(api_key=api_key)

        # Setup model
        self.model = genai.GenerativeModel(
            model_name=model_name,
            system_instruction=SYSTEM_PROMPT,
            tools=tools,
        )
        self.chat = self.model.start_chat(history=[])
        self.tools_mapping = tools_mapping
        logger.info(f"Initialized Gemini Assistant with model: {model_name}")

    # helper function to call the function
    def _call_function(self, function_name, **kwargs):
        return self.tools_mapping[function_name](**kwargs)

    def ask(self, user_input: str) -> str:
        try:
            logger.info(f"Sending message to Gemini Assistant: {user_input}")
            response = self.chat.send_message(user_input)

            # Handle tool calls
            for part in response.candidates[0].content.parts:
                logger.info(f"Received part from Gemini Assistant: {part}")

                if part.function_call:
                    logger.info("Tool call detected")
                    function_call = part.function_call

                    # Call the tool with arguments
                    logger.info(
                        f"Calling tool: {function_call.name} with args: {function_call.args}"
                    )
                    tool_result = self._call_function(
                        function_call.name, **function_call.args
                    )

                    response = self.chat.send_message(f"The tool result: {tool_result}")
                    answer = response.text
                    logger.info(f"Received response from Gemini Assistant: {answer}")
                    return answer  # Allow only 1 tool call
            answer = response.text
            logger.info(f"Received response from Gemini Assistant: {answer}")
            return answer
        except Exception as exc:
            logger.error(f"Error occurred while talking to the assistant: {exc}")
            raise AssistantConversationError(
                "Error occurred while talking to the assistant."
            ) from exc

    def _get_history(self) -> List[Dict[str, str]]:
        """Returns the full conversation history as a list of message dicts."""
        return self.chat.history

    def _reset_history(self):
        """Clears conversation history."""
        self.chat.history.clear()


if __name__ == "__main__":
    # This code defines a GeminiAssistant class that interacts with the Gemini API,
    # allowing users to send messages, handle tool calls, and maintain conversation history.
    # It includes an example tool and demonstrates how to use the assistant.
    # The assistant can be extended with more tools and functionality as needed.
    # Example query:
    # Is it possible to create a todo item with these parameters? content = Clean, category=Work, due_date=05/07/2025?
    from dotenv import load_dotenv
    from plimp.assistant.tools.todo_tools import create_todo_tool

    load_dotenv()
    tools_mapping = {"create_todo_tool": create_todo_tool}
    assistant = GeminiAssistant(
        api_key=os.getenv("GEMINI_API_KEY"),
        tools=[create_todo_tool],
        tools_mapping=tools_mapping,
    )

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        try:
            response = assistant.ask(user_input)
            print(f"Conversation History: {assistant._get_history()}")
        except AssistantConversationError as e:
            print("Error:", str(e))
