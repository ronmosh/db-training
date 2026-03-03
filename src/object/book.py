from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    title: str

class BookCreate(BookBase):
    author_id: int

from typing import List
class BookBulkCreate(BaseModel):
    books: List[BookCreate]

class BookResponse(BookBase):
    id: int
    author_id: int

    class Config:
        from_attributes = True
