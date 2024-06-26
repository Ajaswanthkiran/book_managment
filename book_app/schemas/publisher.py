from pydantic import BaseModel,Field

class Publisher(BaseModel):

    name: str = Field(min_length=3,max_length=30)