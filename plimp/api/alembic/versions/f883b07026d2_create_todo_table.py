"""create todo table

Revision ID: f883b07026d2
Revises: 
Create Date: 2025-06-07 18:20:24.965597

"""

from typing import Sequence, Union


# revision identifiers, used by Alembic.
revision: str = "f883b07026d2"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
