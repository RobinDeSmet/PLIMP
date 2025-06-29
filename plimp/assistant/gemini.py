import os
import google.generativeai as genai
from typing import List, Dict
from plimp.assistant.prompts import SYSTEM_PROMPT
from plimp.assistant.exceptions import AssistantConversationError

# from plimp.assistant.logger import logger
from plimp.utils.logger import logger


class GeminiAssistant:
    def __init__(
        self,
        api_key: str,
        model_name: str = "gemini-2.0-flash-exp",
    ):
        if not api_key:
            raise ValueError("Missing API key for Gemini Assistant.")

        genai.configure(api_key=api_key)

        # Setup model
        self.model = genai.GenerativeModel(
            model_name=model_name, system_instruction=SYSTEM_PROMPT
        )
        self.chat = self.model.start_chat(history=[])
        logger.info(f"Initialized Gemini Assistant with model: {model_name}")

    def ask(self, user_input: str) -> str:
        try:
            logger.info(f"Sending message to Gemini Assistant: {user_input}")
            response = self.chat.send_message(user_input)
            answer = response.text
            logger.info(f"Received response from Gemini Assistant: {answer}")
            return answer
        except Exception as exc:
            logger.error(f"Error occurred while talking to the assistant: {exc}")
            raise AssistantConversationError(
                "Error occurred while talking to the assistant."
            ) from exc

    def get_history(self) -> List[Dict[str, str]]:
        """Returns the full conversation history as a list of message dicts."""
        return self.chat.history

    def reset_history(self):
        """Clears conversation history."""
        self.chat.history.clear()


if __name__ == "__main__":
    # This code defines a GeminiAssistant class that interacts with the Gemini API,
    # allowing users to send messages, handle tool calls, and maintain conversation history.
    # It includes an example tool and demonstrates how to use the assistant.
    # The assistant can be extended with more tools and functionality as needed.
    # Example usage:
    from dotenv import load_dotenv

    load_dotenv()

    assistant = GeminiAssistant(
        api_key=os.getenv("GEMINI_API_KEY"),
    )

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        try:
            response = assistant.ask(user_input)
            print(f"Conversation History: {assistant.get_history()}")
        except AssistantConversationError as e:
            print("Error:", str(e))
