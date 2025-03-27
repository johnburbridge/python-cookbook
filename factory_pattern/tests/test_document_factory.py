import unittest
import os
import tempfile
from factory_pattern.document import Document
from factory_pattern.document_factory import DocumentFactory
from factory_pattern.document_types import DocumentType, PDFDocument, WordDocument, HTMLDocument


class TestDocumentFactory(unittest.TestCase):
    """
    Test cases for the document factory implementation.
    """

    def setUp(self):
        """
        Set up test data.
        """
        self.title = "Test Document"
        self.author = "Test Author"
        self.content = "This is test content for the document."

    def test_create_pdf_document(self):
        """
        Test creating a PDF document.
        """
        # Create a PDF document
        document = DocumentFactory.create_document(
            DocumentType.PDF, self.title, self.author, self.content
        )

        # Verify document type
        self.assertIsInstance(document, PDFDocument)

        # Verify document properties
        self.assertEqual(document.title, self.title)
        self.assertEqual(document.author, self.author)
        self.assertEqual(document.content, self.content)

        # Check document metadata
        self.assertEqual(document.get_metadata("format"), "PDF")
        self.assertEqual(document.get_metadata("version"), "1.7")

    def test_create_word_document(self):
        """
        Test creating a Word document.
        """
        # Create a Word document
        document = DocumentFactory.create_document(
            DocumentType.WORD, self.title, self.author, self.content
        )

        # Verify document type
        self.assertIsInstance(document, WordDocument)

        # Verify document properties
        self.assertEqual(document.title, self.title)
        self.assertEqual(document.author, self.author)
        self.assertEqual(document.content, self.content)

        # Check document metadata
        self.assertEqual(document.get_metadata("format"), "DOCX")
        self.assertEqual(document.get_metadata("version"), "Office Open XML")

    def test_create_html_document(self):
        """
        Test creating an HTML document.
        """
        # Create an HTML document
        document = DocumentFactory.create_document(
            DocumentType.HTML, self.title, self.author, self.content
        )

        # Verify document type
        self.assertIsInstance(document, HTMLDocument)

        # Verify document properties
        self.assertEqual(document.title, self.title)
        self.assertEqual(document.author, self.author)
        self.assertEqual(document.content, self.content)

        # Check document metadata
        self.assertEqual(document.get_metadata("format"), "HTML")
        self.assertEqual(document.get_metadata("version"), "HTML5")

    def test_invalid_document_type(self):
        """
        Test creating a document with an invalid type.
        """
        # Try to create a document with an invalid type
        with self.assertRaises(ValueError):
            DocumentFactory.create_document(
                "INVALID_TYPE", self.title, self.author, self.content
            )

    def test_register_document_type(self):
        """
        Test registering a new document type.
        """

        # Create a new document class
        class TestDocument(Document):
            def __init__(self, title, author, content=""):
                super().__init__(title, author, content)
                self.add_metadata("format", "TEST")

            def create(self) -> str:
                """Create a test document."""
                return f"TEST:{self.title}:{self.author}:{self.content}"

            def generate(self):
                return f"TEST:{self.title}:{self.author}:{self.content}"

            def save(self, path):
                return True

        # Create a new document type
        class NewDocumentType:
            TEST = 999

        # Register the new document type
        DocumentFactory.register_document_type(NewDocumentType.TEST, TestDocument)

        # Create a document with the new type
        document = DocumentFactory.create_document(
            NewDocumentType.TEST, self.title, self.author, self.content
        )

        # Verify document type
        self.assertIsInstance(document, TestDocument)

        # Verify document properties
        self.assertEqual(document.title, self.title)
        self.assertEqual(document.author, self.author)
        self.assertEqual(document.content, self.content)

        # Verify document format
        self.assertEqual(document.get_metadata("format"), "TEST")

    def test_pdf_document_generate(self):
        """
        Test generating a PDF document.
        """
        # Create a PDF document
        document = DocumentFactory.create_document(
            DocumentType.PDF, self.title, self.author, self.content
        )

        # Generate the document
        output = document.generate()

        # Verify PDF content
        self.assertIn("%PDF-1.7", output)
        self.assertIn(self.title, output)
        self.assertIn(self.author, output)
        self.assertIn(self.content, output)

    def test_word_document_generate(self):
        """
        Test generating a Word document.
        """
        # Create a Word document
        document = DocumentFactory.create_document(
            DocumentType.WORD, self.title, self.author, self.content
        )

        # Generate the document
        output = document.generate()

        # Verify Word content
        self.assertIn('<?xml version="1.0"', output)
        self.assertIn(self.title, output)
        self.assertIn(self.author, output)
        self.assertIn(self.content, output)

    def test_html_document_generate(self):
        """
        Test generating an HTML document.
        """
        # Create an HTML document
        document = DocumentFactory.create_document(
            DocumentType.HTML, self.title, self.author, self.content
        )

        # Generate the document
        output = document.generate()

        # Verify HTML content
        self.assertIn("<!DOCTYPE html>", output)
        self.assertIn(self.title, output)
        self.assertIn(self.author, output)
        self.assertIn(self.content, output)

    def test_save_documents(self):
        """
        Test saving documents to files.
        """
        # Create temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Test saving PDF document
            pdf_document = DocumentFactory.create_document(
                DocumentType.PDF, self.title, self.author, self.content
            )
            pdf_path = os.path.join(temp_dir, "test.pdf")
            self.assertTrue(pdf_document.save(pdf_path))
            self.assertTrue(os.path.exists(pdf_path))

            # Test saving Word document
            word_document = DocumentFactory.create_document(
                DocumentType.WORD, self.title, self.author, self.content
            )
            word_path = os.path.join(temp_dir, "test.docx")
            self.assertTrue(word_document.save(word_path))
            self.assertTrue(os.path.exists(word_path))

            # Test saving HTML document
            html_document = DocumentFactory.create_document(
                DocumentType.HTML, self.title, self.author, self.content
            )
            html_path = os.path.join(temp_dir, "test.html")
            self.assertTrue(html_document.save(html_path))
            self.assertTrue(os.path.exists(html_path))

    def test_document_metadata(self):
        """
        Test document metadata.
        """
        # Create a document
        document = DocumentFactory.create_document(
            DocumentType.PDF, self.title, self.author, self.content
        )

        # Verify metadata
        self.assertEqual(document.get_metadata("format"), "PDF")
        self.assertEqual(document.get_metadata("version"), "1.7")
        self.assertEqual(document.get_metadata("title"), self.title)
        self.assertEqual(document.get_metadata("author"), self.author)

        # Test non-existent metadata
        self.assertIsNone(document.get_metadata("non_existent"))


if __name__ == "__main__":
    unittest.main()
