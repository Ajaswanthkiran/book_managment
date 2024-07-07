

from pydantic import BaseModel,Field,EmailStr,field_validator

class User(BaseModel):

    name:str =Field(max_length=15,min_length=3)
    user_name: str=Field(max_length=15,min_length=3)
    password: str=Field(max_length=15,min_length=3)
    mail: EmailStr = Field(max_length=35,min_length=3)
    @field_validator('password')
    def password_must_contain_required_characters(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not any(char.isalpha() for char in v):
            raise ValueError('Password must contain at least one letter')
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one digit')
        if not any(char in '@$!%*#?&' for char in v):
            raise ValueError('Password must contain at least one special character (@$!%*#?&)')
        return v


class UserOut(BaseModel):

    name:str =Field(max_length=15,min_length=3)
    user_name: str=Field(max_length=15,min_length=3)
    mail: EmailStr = Field(max_length=35,min_length=3)
    
class UpdateUser(BaseModel):

    name:str =Field(max_length=15,min_length=3)
    password:str =Field(max_length=15,min_length=3)
    mail: EmailStr = Field(max_length=35,min_length=3)
    @field_validator('password')
    def password_must_contain_required_characters(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not any(char.isalpha() for char in v):
            raise ValueError('Password must contain at least one letter')
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one digit')
        if not any(char in '@$!%*#?&' for char in v):
            raise ValueError('Password must contain at least one special character (@$!%*#?&)')
        return v