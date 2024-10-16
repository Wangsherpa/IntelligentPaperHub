from sqlalchemy import Column, DateTime, String, Text, Integer
from app.db.session import Base


class Paper(Base):
    __tablename__ = "papers"

    id = Column(Integer, primary_key=True, index=True)
    arxiv_id = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=False)
    authors = Column(String)
    abstract = Column(Text, nullable=False)
    update_date = Column(DateTime)
    extracted_content = Column(Text)

    def __repr__(self):
        return f"<Paper(title={self.title}, arxiv_id={self.arxiv_id})>"
