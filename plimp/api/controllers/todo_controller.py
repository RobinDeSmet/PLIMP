from sqlalchemy.orm import Session

from plimp.api.database.models import Todo
from plimp.api.schemas.todo import TodoCreate, TodoUpdate
from plimp.api.utils.exceptions import TodoNotFound
from plimp.api.utils.logger import logger


def create(db: Session, todo_in: TodoCreate) -> Todo:
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


def get(db: Session, todo_id: int) -> Todo:
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        logger.warning(f"Todo with ID {todo_id} not found")
        raise TodoNotFound(f"Todo with ID {todo_id} not found")
    return todo


def list(db: Session, skip: int = 0, limit: int = 100) -> list[Todo]:
    return db.query(Todo).offset(skip).limit(limit).all()


def update(db: Session, todo_id: int, todo_in: TodoUpdate) -> Todo:
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        logger.warning(f"Todo with ID {todo_id} not found")
        raise TodoNotFound(f"Todo with ID {todo_id} not found")
    for field, value in todo_in.model_dump(exclude_unset=True).items():
        setattr(todo, field, value)
    try:
        db.commit()
        db.refresh(todo)
        logger.info(f"Updated todo with ID {todo.id}")
        return todo
    except Exception as e:
        logger.error(f"Error updating todo: {e}")
        db.rollback()
        raise


def delete(db: Session, todo_id: int) -> None:
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        logger.warning(f"Todo with ID {todo_id} not found")
        raise TodoNotFound(f"Todo with ID {todo_id} not found")
    try:
        db.delete(todo)
        db.commit()
        logger.info(f"Deleted todo with ID {todo_id}")
    except Exception as e:
        logger.error(f"Error deleting todo: {e}")
        db.rollback()
        raise
