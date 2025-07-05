from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column
from plimp.api.database.base import Base


class Todo(Base):
    __tablename__ = "todo"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String, nullable=False)
    progress: Mapped[int] = mapped_column(Integer, nullable=False)
    due_date: Mapped[Date | None] = mapped_column(Date, nullable=True)
    category: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self) -> str:
        return (
            f"<Todo(id={self.id}, content='{self.content}', progress={self.progress}, "
            f"due_date={self.due_date}, category='{self.category}')>"
        )
