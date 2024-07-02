

from pydantic import BaseModel,Field


def Page(BaseModel):
    page: int = Field(ge=0)
    size: int =Field(ge=0)
    