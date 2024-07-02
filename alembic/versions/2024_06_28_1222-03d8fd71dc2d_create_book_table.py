"""create book table

Revision ID: 03d8fd71dc2d
Revises: dc40d969b642
Create Date: 2024-06-28 12:22:22.200489

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03d8fd71dc2d'
down_revision: Union[str, None] = 'dc40d969b642'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('author_user_name', sa.String(), nullable=True),
    sa.Column('publisher_name', sa.String(), nullable=True),
    sa.Column('publication_date', sa.Date(), nullable=False),
    sa.Column('isbn', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['author_user_name'], ['sample.author.user_name'], ),
    sa.ForeignKeyConstraint(['publisher_name'], ['sample.publisher.name'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='sample'
    )
    op.create_index(op.f('ix_sample_books_author_user_name'), 'books', ['author_user_name'], unique=False, schema='sample')
    op.create_index(op.f('ix_sample_books_title'), 'books', ['title'], unique=True, schema='sample')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_sample_books_title'), table_name='books', schema='sample')
    op.drop_index(op.f('ix_sample_books_author_user_name'), table_name='books', schema='sample')
    op.drop_table('books', schema='sample')
    # ### end Alembic commands ###