"""change_title_length_in_vocabularies_table

Revision ID: dc8263accd76
Revises: f2a3464bb123
Create Date: 2025-07-08 00:06:13.961069

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc8263accd76'
down_revision: Union[str, Sequence[str], None] = 'f2a3464bb123'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        table_name='vocabularies',
        column_name='title',
        type_=sa.String(25),
        existing_type=sa.String(21),
        nullable=False
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        table_name='vocabularies',
        column_name='title',
        type_=sa.String(21),
        existing_type=sa.String(25),
        nullable=False
    )