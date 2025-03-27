"""Document factory implementation."""

from typing import Dict, Type, Union
from .document import Document
from .document_types import (
    PDFDocument,
    WordDocument,
    HTMLDocument,
    DocumentType,
)


class DocumentFactory:
    """Factory for creating different types of documents."""

    _document_types: Dict[str, Type[Document]] = {
        DocumentType.PDF.value: PDFDocument,
        DocumentType.WORD.value: WordDocument,
        DocumentType.HTML.value: HTMLDocument,
    }

    @classmethod
    def create_document(
        cls,
        doc_type: Union[DocumentType, str, int],
        title: str,
        author: str,
        content: str,
    ) -> Document:
        """
        Create a document of the specified type.

        Args:
            doc_type: The type of document to create (pdf, word, html)
            title: The document title
            author: The document author
            content: The document content

        Returns:
            A new document instance of the specified type

        Raises:
            ValueError: If the document type is not supported
        """
        if isinstance(doc_type, DocumentType):
            doc_type = doc_type.value
        elif isinstance(doc_type, str):
            doc_type = doc_type.lower()

        doc_type_str = str(doc_type)
        if doc_type_str not in cls._document_types:
            supported = ", ".join(cls._document_types.keys())
            raise ValueError(
                f"Unsupported document type: {doc_type}. "
                f"Supported types are: {supported}"
            )

        document_class = cls._document_types[doc_type_str]
        return document_class(title, author, content)

    @classmethod
    def register_document_type(
        cls, doc_type: Union[str, DocumentType, int], document_class: Type[Document]
    ) -> None:
        """
        Register a new document type.

        Args:
            doc_type: The document type enum, string, or integer
            document_class: The class to instantiate for this document type
        """
        if isinstance(doc_type, DocumentType):
            doc_type = doc_type.value
        cls._document_types[str(doc_type)] = document_class

    @classmethod
    def get_registered_types(cls) -> Dict[str, Type[Document]]:
        """
        Get all registered document types.

        Returns:
            A dictionary mapping document types to their classes
        """
        return cls._document_types.copy()
