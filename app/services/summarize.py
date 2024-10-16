import sys

sys.path.append("/Users/wangsherpa/Desktop/my_pc/Projects/IntelligentPaperHub")

from app.openai_utils import create_completion
from app.chunking.chunker import ChunkingStrategy
from app.prompt_templates.summary import (
    BASIC_SUMMARIZER_TEMPLATE,
    REFINE_SUMMARIZER_TEMPLATE,
)


def generate_summary(
    document: str, strategy: str = "refine", chunking_strategy: ChunkingStrategy = None
):
    """Summarize the document using different strategies.

    Args:
        document (str): The given text document to summarize.
        strategy (str, optional): Summarization strategy ('refine', 'standard'). Defaults to "refine".
        chunking_strategy (ChunkingStrategy, optional): Chunking strategy for chunking the document if it's too large. Defaults to None.

    Returns:
        str: Summary of the given document.
    """
    chunks = chunking_strategy.chunk(document)
    if strategy == "standard":
        prompt = BASIC_SUMMARIZER_TEMPLATE.format(text_document=document)
        response = create_completion(prompt=prompt)
        return response.choices[0].message.content

    elif strategy == "refine":
        for i, chunk in enumerate(chunks[:2]):
            final_prompt = BASIC_SUMMARIZER_TEMPLATE.format(text_document=chunk)
            if i > 0:
                final_prompt = REFINE_SUMMARIZER_TEMPLATE.format(
                    previous_summary=summary, text_document=chunk
                )
            summary = create_completion(final_prompt).choices[0].message.content
        return summary
    else:
        raise Exception(
            f"Summarization strategy not supported {strategy} not in ['refine', 'standard']"
        )


if __name__ == "__main__":
    import fitz
    from app.chunking.chunker import ChunkBySeparators

    doc = fitz.open(
        "/Users/wangsherpa/Desktop/my_pc/Projects/paper_recommendation/downloads/test_paper.pdf"
    )
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()

    cs = ChunkBySeparators(
        separators=[".", "\n\n"],
        max_length=4000,
        overlap_percentage=0.1,
    )
    print("[INFO] Generating summary...\n")
    summary = generate_summary(text, chunking_strategy=cs)
    print(summary)
    print("\nSummary Length:", len(summary))
