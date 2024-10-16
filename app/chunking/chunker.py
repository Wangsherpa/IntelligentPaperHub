from abc import ABC, abstractmethod
from typing import List


class ChunkingStrategy(ABC):
    @abstractmethod
    def chunk(self, document: str) -> List[str]:
        """Abstract method for chunking a document into smaller chunks.

        Args:
            document (str): Document to be chunked.

        Returns:
            List[str]: Document chunks.
        """
        pass


class ChunkBySeparators(ChunkingStrategy):
    def __init__(
        self,
        separators: list = [".", "\n\n"],
        max_length: int = 4000,
        overlap_percentage: float = 0.1,
    ):
        """Initialize chunking parameters.

        Args:
            separators (list, optional): List of separators to be used for chunking. Defaults to [".", "\n\n"].
            max_length (int, optional): if separators are not found then this will be used. Defaults to 4000.
            overlap_percentage (float, optional): Overlap percentage between chunks. Defaults to 0.1.
        """
        self.separators = separators
        self.max_length = max_length
        self.overlap_percentage = overlap_percentage

    def chunk(
        self,
        text: str,
    ):
        """Chunk the document using separators and maximum character length.

        Args:
            text (str): The given text document.

        Returns:
            list[str]: List of chunks.
        """
        if len(text) < self.max_length:
            return [text]

        buffer_range = 15  # buffer to search for separators around max length
        chunk_end = min(len(text), self.max_length)

        # Try to find the nearest separator before or slightly after the self.max_length
        best_split = -1
        for separator in self.separators:
            nearby_index = text.rfind(
                separator, chunk_end - buffer_range, chunk_end + buffer_range
            )
            if nearby_index != -1:
                best_split = nearby_index + len(separator)

        if best_split != -1:
            chunk = text[:best_split].strip()
            remaining_text = text[best_split:].strip()
        else:
            chunk = text[: self.max_length].strip()
            remaining_text = text[self.max_length :].strip()

        # handling overlap
        overlap_length = int(len(chunk) * self.overlap_percentage)

        if overlap_length > 0 and len(chunk) > overlap_length:
            overlap_chunk = chunk[-overlap_length:].strip()
        else:
            overlap_chunk = ""

        if overlap_chunk:
            next_text = overlap_chunk + " " + remaining_text
        else:
            next_text = remaining_text

        return [chunk] + self.chunk(next_text)
