from sqlalchemy.orm import Session
from entities.author import Author
from object.author import AuthorCreate

class AuthorRepository:
    def get_all(self, db: Session):
        authors = db.query(Author).all()
        for author in authors:
            author.books = author.books
        return authors

    def get_by_id(self, db: Session, author_id: int):
        return db.query(Author).filter(Author.id == author_id).first()

    def create(self, db: Session, author: AuthorCreate):
        db_author = Author(name=author.name, bio=author.bio)
        db.add(db_author)
        db.commit()
        db.refresh(db_author)
        return db_author
