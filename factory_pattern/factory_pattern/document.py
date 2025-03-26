"""Base document class for the Factory Pattern example."""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class Document(ABC):
    """
    Abstract base class for all document types.

    This class defines the common interface for all document types.
    """

    def __init__(self, title: str, author: str, content: str = "") -> None:
        """
        Initialize a new document.

        Args:
            title: The document title
            author: The document author
            content: The document content (default is empty string)
        """
        self.title = title
        self.author = author
        self.content = content
        self._metadata: Dict[str, Any] = {
            "title": title,
            "author": author,
        }

    def add_metadata(self, key: str, value: Any) -> None:
        """
        Add metadata to the document.

        Args:
            key: The metadata key
            value: The metadata value
        """
        self._metadata[key] = value

    def get_metadata(self, key: str) -> Optional[Any]:
        """
        Get metadata from the document.

        Args:
            key: The metadata key

        Returns:
            Optional[Any]: The metadata value or None if the key doesn't exist
        """
        return self._metadata.get(key)

    @abstractmethod
    def create(self) -> str:
        """
        Create the document content.

        Returns:
            The formatted document content
        """
        pass

    @abstractmethod
    def save(self, path: str) -> bool:
        """
        Save the document to a file.

        Args:
            path: The path where to save the document

        Returns:
            bool: True if the document was saved successfully, False otherwise
        """
        pass
