"""add_unique_constraint_to_title

Revision ID: 7cae82440164
Revises: dc8263accd76
Create Date: 2025-07-09 22:00:22.451172

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '7cae82440164'
down_revision: Union[str, Sequence[str], None] = 'dc8263accd76'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_unique_constraint("uq_vocabularies_title", "vocabularies", ["title"])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("uq_vocabularies_title", "vocabularies", type_="unique")
