from sqlmodel import Session
from app.utils.db import engine

def get_session():
    with Session(engine) as session:
        yield session
