from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class Author(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)
    email: str = Field(max_length=50, unique=True, index=True)
    age: Optional[int] = None 
    books: List["Book"] = Relationship(back_populates="author")

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=100)
    content: str
    author_id: int = Field(foreign_key="author.id")

    author: Optional[Author] = Relationship(back_populates="books")
