from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


DB_URL = "sqlite:///./data.db"


engine = create_engine(
    DB_URL,
    connect_args={
        "check_same_thread": False
    }
)


class Base(DeclarativeBase): pass


SessionLocal = sessionmaker(bind=engine, autoflush=False)