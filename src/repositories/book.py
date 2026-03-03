from sqlalchemy.orm import Session
from entities.book import Book
from object.book import BookCreate

class BookRepository:
    def get_all(self, db: Session):
        return db.query(Book).all()

    def get_by_id(self, db: Session, book_id: int):
        return db.query(Book).filter(Book.id == book_id).first()

    def create(self, db: Session, book: BookCreate):
        db_book = Book(title=book.title, author_id=book.author_id)
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book
    
    def get_by_author(self, db: Session, author_id: int):
        return db.query(Book).filter(Book.author_id == author_id).all()
