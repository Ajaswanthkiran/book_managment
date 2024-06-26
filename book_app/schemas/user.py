

from pydantic import BaseModel,Field,EmailStr

class User(BaseModel):

    name:str =Field(max_length=15,min_length=3)
    user_name=Field(max_length=15,min_length=3)
    password=Field(max_length=15,min_length=3)
    mail: EmailStr = Field(max_length=15,min_length=3)
    