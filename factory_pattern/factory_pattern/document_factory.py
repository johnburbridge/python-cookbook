"""Document factory implementation."""

from typing import Dict, Type
from .document import Document
from .document_types import (
    PDFDocument,
    WordDocument,
    HTMLDocument,
)


class DocumentFactory:
    """Factory for creating different types of documents."""

    _document_types: Dict[str, Type[Document]] = {
        "pdf": PDFDocument,
        "word": WordDocument,
        "html": HTMLDocument,
    }

    @classmethod
    def create_document(cls, doc_type: str, title: str, content: str) -> Document:
        """
        Create a document of the specified type.

        Args:
            doc_type: The type of document to create (pdf, word, html)
            title: The document title
            content: The document content

        Returns:
            A new document instance of the specified type

        Raises:
            ValueError: If the document type is not supported
        """
        doc_type = doc_type.lower()
        if doc_type not in cls._document_types:
            supported = ", ".join(cls._document_types.keys())
            raise ValueError(
                f"Unsupported document type: {doc_type}. "
                f"Supported types are: {supported}"
            )

        document_class = cls._document_types[doc_type]
        return document_class(title, content)

    @classmethod
    def register_document_type(
        cls, doc_type: str, document_class: Type[Document]
    ) -> None:
        """
        Register a new document type.

        Args:
            doc_type: The document type enum
            document_class: The class to instantiate for this document type
        """
        cls._document_types[doc_type] = document_class

    @classmethod
    def get_registered_types(cls) -> Dict[str, Type[Document]]:
        """
        Get all registered document types.

        Returns:
            A dictionary mapping document types to their classes
        """
        return cls._document_types.copy()
