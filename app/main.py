from fastapi import FastAPI
from app.api.routers import paper

app = FastAPI()
app.include_router(paper.router)


@app.get("/")
async def root():
    return {"message": "The API is running..."}
