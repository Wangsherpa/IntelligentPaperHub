from sqlalchemy.orm import Session
from app.db.session import engine, Base


# Function to initialize the database and create tables
def init_db():
    Base.metadata.create_all(bind=engine)


# Function to seed any inital data if required
def seed_db(db: Session):
    # TODO: Add initial data to the database
    pass
