from pydantic import BaseModel,Field

class Publisher(BaseModel):

    name: str = Field(min_length=3,max_length=30)
    password: str= Field(min_length=3,max_length=30) 

class PublisherOut(BaseModel):
    name: str = Field(min_length=3,max_length=30)