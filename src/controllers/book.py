from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from object.book import BookCreate, BookResponse, BookBulkCreate
from services.book import BookService

router = APIRouter(prefix="/books", tags=["books"])
service = BookService()

@router.get("/", response_model=List[BookResponse])
def get_books(db: Session = Depends(get_db)):
    return service.get_all_books(db)

@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = service.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=BookResponse, status_code=201)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    # Basic validation for author existence could be handled in service, simplified here
    return service.create_book(db, book)

@router.post("/bulk", response_model=List[BookResponse], status_code=201)
def create_books_bulk(bulk_data: BookBulkCreate, db: Session = Depends(get_db)):
    return service.create_books_bulk(db, bulk_data)
