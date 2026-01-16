from fastapi import APIRouter, Depends
from sqlmodel import select, Session
from app.models.models import Book
from app.utils.deps import get_session
from typing import Optional

router = APIRouter()

@router.post("/", response_model=Book)
def create_book(book: Book, session: Session = Depends(get_session)):
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

@router.get("/", response_model=list[Book])
def get_books(author_id: Optional[int] = None, session: Session = Depends(get_session)):
    statement = select(Book)

    if author_id is not None:
        statement = statement.where(Book.author_id == author_id)

    return session.exec(statement).all()
