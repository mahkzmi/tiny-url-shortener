from sqlmodel import create_engine, SQLModel, Session
import os

DATABASE_URL=os.getenv("DATABASE_URL", "sqlite:///./shortener.db")
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, echo=False, connect_args = connect_args)



def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session