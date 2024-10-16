from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:////Users/wangsherpa/Desktop/my_pc/Projects/IntelligentPaperHub/app/db/paper.db"

# create an engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Session Local factory for creating database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
