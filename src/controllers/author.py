from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from object.author import AuthorCreate, AuthorResponse
from services.author import AuthorService

router = APIRouter(prefix="/authors", tags=["authors"])
service = AuthorService()

@router.get("/", response_model=List[AuthorResponse])
def get_authors(db: Session = Depends(get_db)):
    return service.get_all_authors(db)

@router.get("/{author_id}", response_model=AuthorResponse)
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = service.get_author(db, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@router.post("/", response_model=AuthorResponse, status_code=201)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    return service.create_author(db, author)
