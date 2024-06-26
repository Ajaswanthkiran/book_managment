"""creating book,author and publisher table

Revision ID: 22e9f68614f5
Revises: 
Create Date: 2024-06-26 12:15:38.469459

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22e9f68614f5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('user_name', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('mail', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id',name="PK_author_id"),
    sa.UniqueConstraint('mail')
    )
    op.create_index(op.f('ix_author_user_name'), 'author', ['user_name'], unique=True)
    op.create_table('publisher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id',name="PK_publisher_id"),
    sa.UniqueConstraint('name')
    )
    op.create_table('books',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('author_user_name', sa.String(), nullable=True),
    sa.Column('publisher_name', sa.String(), nullable=True),
    sa.Column('publication_data', sa.Date(), nullable=False),
    sa.Column('isbn', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['author_user_name'], ['author.user_name'], name="FK_books_author_user_name_author_user_name"),
    sa.ForeignKeyConstraint(['publisher_name'], ['publisher.name'], name="FK_books_publisher_name_publisher_name"),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_books_id'), 'books', ['id'], unique=False)
    op.create_index(op.f('ix_books_title'), 'books', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_books_title'), table_name='books')
    op.drop_index(op.f('ix_books_id'), table_name='books')
    op.drop_table('books')
    op.drop_table('publisher')
    op.drop_index(op.f('ix_author_user_name'), table_name='author')
    op.drop_table('author')
    # ### end Alembic commands ###