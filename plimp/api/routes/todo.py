from http.client import HTTPException
from fastapi import APIRouter, Depends, status

from plimp.api.database.session import get_session
from plimp.api.schemas.todo import TodoCreate, TodoRead
from sqlalchemy.orm import Session
from plimp.api.controllers import todo_controller


router = APIRouter(tags=["todo"], prefix="/todo", include_in_schema=True)


@router.post("/", response_model=TodoRead, status_code=status.HTTP_201_CREATED)
def create_todo(todo_in: TodoCreate, db: Session = Depends(get_session)) -> TodoRead:
    try:
        return todo_controller.create_todo(db, todo_in)
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create todo: {str(e)}",
        )
