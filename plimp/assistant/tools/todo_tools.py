from datetime import datetime

from plimp.api.controllers import todo_controller
from plimp.api.database.session import get_tools_session
from plimp.api.database.models import Todo
from plimp.api.schemas.todo import TodoCreate


def create_todo_tool(
    content: str, category: str, progress: int | None, due_date_string: str | None
) -> Todo:
    """
    Creates a new todo item with the provided parameters.

    Args:
        content (str): The content of the todo item.
        category (str): The category of the todo item.
        progress (int | None): The progress of the todo item (0-100). Defaults to 0.
        due_date (str | None): The due date of the todo item. Must be in the future and follows the format DD/MM/YYYY

    Returns:
        Todo: The created todo item.
    """
    # Convert parameters
    due_date = (
        datetime.strptime(due_date_string, "%d/%m/%Y").date()
        if due_date_string
        else None
    )

    # Create a TodoCreate object with the provided parameters
    create_todo_object = TodoCreate(
        content=content, progress=progress, due_date=due_date, category=category
    )
    # Call the create function from the todo_controller
    return todo_controller.create(db=get_tools_session(), todo_in=create_todo_object)


def get_todo_info_tool() -> list[str]:
    """
    Fetches all todo items from the database, so you can answer questions about them.
    For example, if somebody asks "What todo item should I focus on today?",
    you can use this tool to get the list of todo items and find the one that is most relevant.

    Returns:
        list[str]: List of all todo items in readable format.
    """
    todo_items = todo_controller.list(db=get_tools_session())
    readable_todo_items = [str(item) for item in todo_items]
    return readable_todo_items
