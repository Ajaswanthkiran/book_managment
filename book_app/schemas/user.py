

from pydantic import BaseModel,Field,EmailStr

class User(BaseModel):

    name:str =Field(max_length=15,min_length=3)
    user_name: str=Field(max_length=15,min_length=3)
    password: str=Field(max_length=15,min_length=3)
    mail: EmailStr = Field(max_length=35,min_length=3)
    
class UpdateUser(BaseModel):

    name:str =Field(max_length=15,min_length=3)
    password:str =Field(max_length=15,min_length=3)
    mail: EmailStr = Field(max_length=35,min_length=3)
    