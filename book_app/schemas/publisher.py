from pydantic import BaseModel,Field,field_validator

class Publisher(BaseModel):

    name: str = Field(min_length=3,max_length=30)
    password: str= Field(min_length=3,max_length=30) 
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

class PublisherOut(BaseModel):
    name: str = Field(min_length=3,max_length=30)