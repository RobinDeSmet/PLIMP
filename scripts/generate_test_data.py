from datetime import date, timedelta

from plimp.api.schemas.todo import TodoCreate
from plimp.api.database.session import get_tools_session
from plimp.api.controllers import todo_controller
from plimp.utils.logger import logger


def generate_test_todos():
    return [
        TodoCreate(
            content="Buy groceries",
            progress=0,
            due_date=date.today() + timedelta(days=1),
            category="Personal",
        ),
        TodoCreate(
            content="Finish project report",
            progress=50,
            due_date=date.today() + timedelta(days=3),
            category="Work",
        ),
        TodoCreate(
            content="Call plumber",
            progress=20,
            due_date=date.today() + timedelta(days=2),
            category="Home",
        ),
        TodoCreate(
            content="Plan vacation",
            progress=10,
            due_date=date.today() + timedelta(days=10),
            category="Leisure",
        ),
        TodoCreate(
            content="Read book",
            progress=80,
            due_date=date.today() + timedelta(days=5),
            category="Personal",
        ),
        TodoCreate(
            content="Pay electricity bill",
            progress=100,
            due_date=date.today(),
            category="Finance",
        ),
        TodoCreate(
            content="Clean the garage",
            progress=30,
            due_date=date.today() + timedelta(days=4),
            category="Home",
        ),
        TodoCreate(
            content="Schedule dentist appointment",
            progress=0,
            due_date=date.today() + timedelta(days=7),
            category="Health",
        ),
        TodoCreate(
            content="Write blog post",
            progress=40,
            due_date=date.today() + timedelta(days=6),
            category="Writing",
        ),
        TodoCreate(
            content="Organize photo album",
            progress=60,
            due_date=date.today() + timedelta(days=8),
            category="Personal",
        ),
        TodoCreate(
            content="Back up laptop",
            progress=90,
            due_date=date.today() + timedelta(days=1),
            category="Tech",
        ),
        TodoCreate(
            content="Submit tax documents",
            progress=20,
            due_date=date.today() + timedelta(days=2),
            category="Finance",
        ),
        TodoCreate(
            content="Research new phone",
            progress=10,
            due_date=date.today() + timedelta(days=9),
            category="Shopping",
        ),
        TodoCreate(
            content="Water garden",
            progress=0,
            due_date=date.today() + timedelta(days=1),
            category="Home",
        ),
        TodoCreate(
            content="Update LinkedIn profile",
            progress=75,
            due_date=date.today() + timedelta(days=5),
            category="Career",
        ),
    ]


def main():
    try:
        todos = generate_test_todos()
        for todo_in in todos:
            todo_controller.create(db=get_tools_session(), todo_in=todo_in)
    except Exception as e:
        logger.error(f"Test script failed: {e}")


if __name__ == "__main__":
    main()
