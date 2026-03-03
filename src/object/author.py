from pydantic import BaseModel
from typing import Optional, List
from .book import BookResponse

class AuthorBase(BaseModel):
    name: str
    bio: Optional[str] = None

class AuthorCreate(AuthorBase):
    pass

class AuthorResponse(AuthorBase):
    id: int
    books: List[BookResponse] = []

    class Config:
        from_attributes = True
