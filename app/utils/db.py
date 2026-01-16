from sqlmodel import SQLModel, create_engine

DATABASE_URL = "postgresql://postgres:9868@localhost:5432/library_db"

engine = create_engine(DATABASE_URL)

def init_db():
    SQLModel.metadata.create_all(engine)
