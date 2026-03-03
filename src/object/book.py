from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    title: str

class BookCreate(BookBase):
    author_id: int

class BookResponse(BookBase):
    id: int
    author_id: int

    class Config:
        from_attributes = True
