from fastapi import FastAPI
from app.utils.db import init_db
from app.routes.authors import router as author_router
from app.routes.books import router as book_router

app = FastAPI(title="FastAPI SQLModel PostgreSQL Example")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(author_router, prefix="/authors", tags=["Authors"])
app.include_router(book_router, prefix="/books", tags=["Books"])
