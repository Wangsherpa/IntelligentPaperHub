from pydantic import BaseModel, Field
from typing import Optional


class ChunkBySeparatorModel(BaseModel):
    separators: list[str] = [".", "\n\n"]
    max_length: int = 4000  # characters
    overlap_percentage: float = Field(
        gt=0, le=0.5, description="Overlap % between adjacent chunks"
    )


class ChunkRequestModel(BaseModel):
    chunking_strategy: str = "separators"
    parameters: Optional[dict]
