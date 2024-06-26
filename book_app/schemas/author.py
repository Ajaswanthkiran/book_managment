

from pydantic import BaseModel,Field,EmailStr

class Author(BaseModel):

    name: str =Field(max_length=15,min_length=3)
    user_name: str =Field(max_length=15,min_length=3)
    password: str =Field(max_length=15,min_length=3)
    mail: EmailStr =Field(max_length=25,min_length=3)
