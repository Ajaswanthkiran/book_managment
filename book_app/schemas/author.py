

from pydantic import BaseModel,Field,EmailStr

class Author(BaseModel):

    name: str =Field(max_length=15,min_length=3)
    user_name: str =Field(max_length=15,min_length=3)
    password: str =Field(max_length=15,min_length=3)
    mail: EmailStr =Field(max_length=35,min_length=3)

class AuthorUpdate(BaseModel):
    name: str =Field(max_length=15,min_length=3)
    password: str =Field(max_length=15,min_length=3)
    mail: EmailStr =Field(max_length=35,min_length=3)


class AuthorOut(BaseModel):
    name: str =Field(max_length=15,min_length=3)
    user_name: str =Field(max_length=15,min_length=3)
    mail: EmailStr =Field(max_length=35,min_length=3)
