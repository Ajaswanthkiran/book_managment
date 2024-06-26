

from sqlalchemy import Column,Integer,String,Date,ForeignKey
from sqlalchemy.orm import relationship
from .author import Author
from .publisher import Publisher

from book_app.db.database import Base


class Book(Base):

    __tablename__="books"
    #pk_book_
    id = Column(Integer,autoincrement=True,primary_key=True,index=True)
    title=Column(String,nullable=False,index=True)
    author_user_name=Column(String,ForeignKey(Author.user_name))
    publisher_name=Column(String,ForeignKey(Publisher.name))
    publication_data=Column(Date,nullable=False)
    isbn=Column(String,nullable=False)
    