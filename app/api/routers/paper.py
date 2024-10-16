import os
import fitz
from fastapi import APIRouter, File, UploadFile
from app.chunking.chunker import ChunkBySeparators
from app.services.summarize import generate_summary

router = APIRouter(prefix="/paper", tags=["Paper"])


async def load_pdf(file: UploadFile) -> str:
    """Process a .pdf file and return its content.

    Args:
        file (UploadFile): The uploaded .pdf file.

    Raises:
        HTTPException: If an unsupported processor is selected.

    Returns:
        str: Extracted text content from the PDF.
    """
    temp_filepath = f"temp_{file.filename}"
    with open(temp_filepath, "wb") as temp_file:
        temp_file.write(await file.read())

    doc = fitz.open(temp_filepath)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    os.remove(temp_filepath)
    return text


# @router.get("/{id}")
@router.post("/summarize")
async def summarize(
    file: UploadFile = File(...),
    summary_strategy: str = "refine",
    chunking_strategy: str = "separators",
):
    chunking_strategies = {"separators": ChunkBySeparators}

    text = await load_pdf(file)
    chunking_strategy = chunking_strategies[chunking_strategy]()
    # summary = generate_summary(
    #     document=text, strategy=summary_strategy, chunking_strategy=chunking_strategy
    # )
    summary = "testing"
    return {"summary": summary}
