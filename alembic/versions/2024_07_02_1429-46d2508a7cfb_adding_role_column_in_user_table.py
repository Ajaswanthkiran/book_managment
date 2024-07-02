""" adding role column in user table

Revision ID: 46d2508a7cfb
Revises: 8a2f66ea5b4e
Create Date: 2024-07-02 14:29:42.617466

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46d2508a7cfb'
down_revision: Union[str, None] = '8a2f66ea5b4e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    
    op.add_column('user', sa.Column('role', sa.String(), nullable=True), schema='sample')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'role', schema='sample')
    # ### end Alembic commands ###
