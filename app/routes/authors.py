from fastapi import APIRouter, Depends
from sqlmodel import select, Session
from app.models.models import Author
from app.utils.deps import get_session
from typing import Optional

router = APIRouter()

@router.post("/", response_model=Author)
def create_author(author: Author, session: Session = Depends(get_session)):
    session.add(author)
    session.commit()
    session.refresh(author)
    return author

@router.get("/", response_model=list[Author])
def get_authors(_id: Optional[int] = None,session: Session = Depends(get_session)):
    statement = select(Author)

    if _id is not None:
        statement = statement.where(Author.id == _id)

    return session.exec(statement).all()
