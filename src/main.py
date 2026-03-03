from fastapi import FastAPI
from controllers.author import router as author_router
from controllers.book import router as book_router

app = FastAPI(
    title="DB Training API",
    description="Training environment for FastAPI, SQLAlchemy, and Alembic.",
    version="1.0.0",
)

app.include_router(author_router)
app.include_router(book_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the DB Training API"}
