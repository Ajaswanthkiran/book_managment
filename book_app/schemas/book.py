

from pydantic import BaseModel,Field,ConfigDict
from datetime import date


class Book(BaseModel):

    title: str =Field(max_length=100,min_length=3)
    author_user_name: str=Field(max_length=100,min_length=3)
    publisher_name: str=Field(max_length=100,min_length=3)
    publication_date: date 
    isbn: str =Field(min_length=13,max_length=13)


class UpdateBook(BaseModel):
    title: str =Field(max_length=100,min_length=3)
    publication_date: date 
    isbn: str =Field(min_length=13,max_length=13)
