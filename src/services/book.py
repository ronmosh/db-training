from sqlalchemy.orm import Session
from repositories.book import BookRepository
from object.book import BookCreate

class BookService:
    def __init__(self):
        self.repository = BookRepository()

    def get_all_books(self, db: Session):
        return self.repository.get_all(db)

    def get_book(self, db: Session, book_id: int):
        return self.repository.get_by_id(db, book_id)

    def create_book(self, db: Session, book: BookCreate):
        return self.repository.create(db, book)
    
    def get_books_by_author(self, db: Session, author_id: int):
        return self.repository.get_by_author(db, author_id)
