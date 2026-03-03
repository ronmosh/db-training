from sqlalchemy.orm import Session
from repositories.author import AuthorRepository
from object.author import AuthorCreate

class AuthorService:
    def __init__(self):
        self.repository = AuthorRepository()

    def get_all_authors(self, db: Session):
        return self.repository.get_all(db)

    def get_author(self, db: Session, author_id: int):
        return self.repository.get_by_id(db, author_id)

    def create_author(self, db: Session, author: AuthorCreate):
        return self.repository.create(db, author)
