from datetime import date
from pydantic import BaseModel, Field, field_validator
from typing import Optional


class TodoBase(BaseModel):
    content: str = Field(..., example="Buy groceries")
    progress: int = Field(..., ge=0, le=100, example=50)
    due_date: Optional[date] = Field(None, example="2025-06-30")
    category: str = Field(..., example="Personal")

    @field_validator("due_date")
    @classmethod
    def validate_due_date(cls, v):
        if v and v < date.today():
            raise ValueError("Due date cannot be in the past!")
        return v

    @field_validator("progress")
    @classmethod
    def validate_progress(cls, v):
        if v and (v < 0 or v > 100):
            raise ValueError("Progress must be a value between 0 and 100!")
        return v


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    content: Optional[str] = None
    progress: Optional[int] = Field(None, ge=0, le=100)
    due_date: Optional[date] = None
    category: Optional[str] = None


class TodoRead(TodoBase):
    id: int

    class Config:
        orm_mode = True
