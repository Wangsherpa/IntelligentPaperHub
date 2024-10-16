import sys
from datetime import datetime

sys.path.append("/Users/wangsherpa/Desktop/my_pc/Projects/IntelligentPaperHub")
from app.db.session import SessionLocal
from app.models.paper import Paper


def test_db():
    db = SessionLocal()

    # Create a new paper
    new_paper = Paper(
        arxiv_id="test1234",
        title="Sample Research Paper",
        authors="Wang, Sherpa",
        abstract="This is a sample abstract for the research paper.",
        update_date=datetime(year=2008, month=4, day=30),
    )

    db.add(new_paper)
    db.commit()

    paper = db.query(Paper).filter(Paper.arxiv_id == "test123").first()
    print(paper)

    db.close()


if __name__ == "__main__":
    from app.db.init_db import init_db

    init_db()
    test_db()
