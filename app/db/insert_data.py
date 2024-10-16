import json
import sys
from datetime import datetime

sys.path.append("/Users/wangsherpa/Desktop/my_pc/Projects/IntelligentPaperHub")
from app.db.session import SessionLocal
from app.models.paper import Paper

dataset_path = "/Users/wangsherpa/Desktop/my_pc/Projects/Datasets/arxiv/arxiv-metadata-oai-snapshot.json"


def get_db():
    with open(dataset_path, "r") as file:
        for line in file:
            yield line


if __name__ == "__main__":
    from datetime import datetime
    from tqdm import tqdm
    from app.db.init_db import init_db

    init_db()

    required_categories = ["cs.AI", "cs.CL", "cs.CV", "cs.NE"]
    paper_meta = get_db()
    db = SessionLocal()
    for data in tqdm(paper_meta):
        data_dict = json.loads(data)
        year, month, day = [int(d) for d in data_dict["update_date"].split("-")]
        update_date = datetime(year=year, month=month, day=day)
        for category in required_categories:
            if category in data_dict["categories"]:
                paper = Paper(
                    arxiv_id=data_dict["id"],
                    title=data_dict["title"],
                    authors=data_dict["authors"],
                    abstract=data_dict["abstract"],
                    update_date=update_date,
                )
                db.add(paper)
                break
    db.commit()
    db.close()
