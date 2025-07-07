"""create vocabularies table

Revision ID: f2a3464bb123
Revises: 
Create Date: 2025-07-07 21:57:56.430491

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f2a3464bb123'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "vocabularies",
        sa.Column("vocabulary_no", sa.Integer, primary_key=True),
        sa.Column("title", sa.String(21), nullable=False),
        sa.Column("meaning", sa.Text, nullable=False),
        sa.Column("sentence", sa.Text, nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("vocabularies")
