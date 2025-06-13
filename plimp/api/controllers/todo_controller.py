from sqlalchemy.orm import Session

from plimp.api.database.models import Todo
from plimp.api.schemas.todo import TodoCreate
from plimp.api.utils.logger import logger


def create_todo(db: Session, todo_in: TodoCreate) -> Todo:
    todo = Todo(**todo_in.model_dump())
    logger.info(f"Creating new todo: {todo_in}")

    try:
        db.add(todo)
        db.commit()
        db.refresh(todo)
        logger.info(f"Created todo with ID {todo.id}")
        return todo
    except Exception as e:
        logger.error(f"Error creating todo: {e}")
        db.rollback()
        raise
