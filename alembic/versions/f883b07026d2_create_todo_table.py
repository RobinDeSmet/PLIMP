"""create todo table

Revision ID: f883b07026d2
Revises:
Create Date: 2025-06-07 18:20:24.965597

"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers
revision: str = "f883b07026d2"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "todo",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("content", sa.String, nullable=False),
        sa.Column("progress", sa.Integer, nullable=False),
        sa.Column("due_date", sa.Date, nullable=True),
        sa.Column("category", sa.String, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("todo")
