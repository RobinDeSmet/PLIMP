from fastapi import APIRouter, Depends, status, HTTPException

from plimp.api.database.session import get_session
from plimp.api.schemas.todo import TodoCreate, TodoRead, TodoUpdate
from sqlalchemy.orm import Session
from plimp.api.controllers import todo_controller
from plimp.api.utils.exceptions import TodoNotFound


router = APIRouter(tags=["todo"], prefix="/todo", include_in_schema=True)


@router.post("/", response_model=TodoRead, status_code=status.HTTP_201_CREATED)
def create(todo_in: TodoCreate, db: Session = Depends(get_session)) -> TodoRead:
    try:
        return todo_controller.create(db, todo_in)
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create todo: {str(e)}",
        )


@router.get("/{todo_id}", response_model=TodoRead)
def get(todo_id: int, db: Session = Depends(get_session)) -> TodoRead:
    try:
        return todo_controller.get(db, todo_id)
    except TodoNotFound:
        raise HTTPException(status_code=404, detail="Todo not found")


@router.get("/", response_model=list[TodoRead])
def list_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    return todo_controller.list(db, skip=skip, limit=limit)


@router.put("/{todo_id}", response_model=TodoRead)
def update(
    todo_id: int, todo_in: TodoUpdate, db: Session = Depends(get_session)
) -> TodoRead:
    try:
        return todo_controller.update(db, todo_id, todo_in)
    except TodoNotFound:
        raise HTTPException(status_code=404, detail="Todo not found")
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to update todo: {str(e)}",
        )


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(todo_id: int, db: Session = Depends(get_session)):
    try:
        todo_controller.delete(db, todo_id)
    except TodoNotFound:
        raise HTTPException(status_code=404, detail="Todo not found")
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to delete todo: {str(e)}",
        )
