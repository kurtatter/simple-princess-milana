"""Add Event.revision: int

Revision ID: 61a9fb0df235
Revises: 99d18e8b2c22
Create Date: 2024-01-30 20:21:45.645688

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '61a9fb0df235'
down_revision: Union[str, None] = '99d18e8b2c22'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Event', sa.Column('revision', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Event', 'revision')
    # ### end Alembic commands ###