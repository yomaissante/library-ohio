"""add new column to table

Revision ID: 0ccafff649ed
Revises: 920eb6027c25
Create Date: 2024-08-29 15:25:42.741047

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ccafff649ed'
down_revision: Union[str, None] = '920eb6027c25'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
