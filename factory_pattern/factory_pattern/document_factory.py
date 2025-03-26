from enum import Enum, auto
from typing import Dict, Type, Optional

from .document import Document
from .document_types import (
    PDFDocument,
    WordDocument,
    HTMLDocument,
    MarkdownDocument,
    TextDocument,
)


class DocumentType(Enum):
    """
    Enum representing different document types.
    """

    PDF = auto()
    WORD = auto()
    HTML = auto()


class DocumentFactory:
    """
    Factory class that creates document objects.
    This is a simple factory implementation.
    """

    # Mapping of document types to their respective classes
    _document_types: Dict[DocumentType, Type[Document]] = {
        DocumentType.PDF: PDFDocument,
        DocumentType.WORD: WordDocument,
        DocumentType.HTML: HTMLDocument,
    }

    @classmethod
    def create_document(
        cls, doc_type: DocumentType, title: str, author: str, content: str = ""
    ) -> Document:
        """
        Create a document of the specified type.

        Args:
            doc_type: The type of document to create
            title: The title of the document
            author: The author of the document
            content: The content of the document (default is empty string)

        Returns:
            Document: A document of the specified type

        Raises:
            ValueError: If the document type is not supported
        """
        document_class = cls._document_types.get(doc_type)

        if document_class is None:
            raise ValueError(f"Unsupported document type: {doc_type}")

        return document_class(title, author, content)

    @classmethod
    def register_document_type(
        cls, doc_type: DocumentType, document_class: Type[Document]
    ) -> None:
        """
        Register a new document type.

        Args:
            doc_type: The document type enum
            document_class: The class to instantiate for this document type
        """
        cls._document_types[doc_type] = document_class

    @classmethod
    def get_registered_types(cls) -> Dict[DocumentType, Type[Document]]:
        """
        Get all registered document types.

        Returns:
            Dict[DocumentType, Type[Document]]: A dictionary mapping document types to their classes
        """
        return cls._document_types.copy()
