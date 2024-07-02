""" adding role column in publisher table

Revision ID: 8a2f66ea5b4e
Revises: 68618ca6f1d6
Create Date: 2024-07-02 14:29:00.534570

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8a2f66ea5b4e'
down_revision: Union[str, None] = '68618ca6f1d6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    
    op.add_column('publisher', sa.Column('role', sa.String(), nullable=True), schema='sample')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('publisher', 'role', schema='sample')
    
    # ### end Alembic commands ###