#!/usr/bin/env python3
"""
This script demonstrates the Factory Pattern with document generation.
It creates different types of documents (PDF, Word, HTML) using a document factory.
"""
import os
import tempfile
from factory_pattern.document_factory import DocumentFactory, DocumentType


def main():
    """
    Main function to demonstrate the Factory Pattern.
    """
    print("Document Factory Pattern Demo")
    print("=============================\n")

    # Create document title and author
    title = "The Factory Pattern"
    author = "Design Patterns"
    content = "The Factory Pattern is a creational design pattern that provides an interface for creating objects."

    # Create documents of different types
    print("Creating documents of different types...\n")

    # Create a PDF document
    pdf_document = DocumentFactory.create_document(
        DocumentType.PDF, title, author, content
    )

    # Create a Word document
    word_document = DocumentFactory.create_document(
        DocumentType.WORD, title, author, content
    )

    # Create an HTML document
    html_document = DocumentFactory.create_document(
        DocumentType.HTML, title, author, content
    )

    # Add custom metadata and css to HTML document
    html_document.add_metadata("keywords", "factory, pattern, design patterns")
    html_document.set_css(
        """
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        header {
            background-color: #f5f5f5;
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }
        h1 {
            color: #2c3e50;
        }
        .author {
            font-style: italic;
            color: #7f8c8d;
        }
        .content {
            line-height: 1.6;
            margin: 20px 0;
        }
        footer {
            margin-top: 30px;
            font-size: 0.8em;
            color: #95a5a6;
            text-align: center;
        }
    """
    )

    # Print document metadata
    print("Document Metadata:")
    print("-----------------")

    print("\nPDF Document:")
    for key, value in pdf_document.metadata.items():
        print(f"  {key}: {value}")

    print("\nWord Document:")
    for key, value in word_document.metadata.items():
        print(f"  {key}: {value}")

    print("\nHTML Document:")
    for key, value in html_document.metadata.items():
        print(f"  {key}: {value}")

    # Demonstrate saving documents to temp files
    print("\n\nSaving documents to temporary files...")

    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Save PDF document
        pdf_path = os.path.join(temp_dir, "document.pdf")
        pdf_document.save(pdf_path)
        print(f"PDF document saved to: {pdf_path}")

        # Save Word document
        word_path = os.path.join(temp_dir, "document.docx")
        word_document.save(word_path)
        print(f"Word document saved to: {word_path}")

        # Save HTML document
        html_path = os.path.join(temp_dir, "document.html")
        html_document.save(html_path)
        print(f"HTML document saved to: {html_path}")

        print("\nDocument content examples:")
        print("-----------------------")

        # Show a snippet of each document's generated content
        print("\nPDF Document (first few lines):")
        pdf_content = pdf_document.generate().split("\n")[:5]
        print("\n".join(pdf_content) + "\n...")

        print("\nWord Document (first few lines):")
        word_content = word_document.generate().split("\n")[:5]
        print("\n".join(word_content) + "\n...")

        print("\nHTML Document (first few lines):")
        html_content = html_document.generate().split("\n")[:5]
        print("\n".join(html_content) + "\n...")

    print("\nTemporary files have been cleaned up.")

    # Demonstrate registering a new document type
    print("\nRegistering a custom document type would work like this:")
    print("DocumentFactory.register_document_type(DocumentType.CUSTOM, CustomDocument)")
    print(
        "custom_doc = DocumentFactory.create_document(DocumentType.CUSTOM, title, author, content)"
    )


if __name__ == "__main__":
    main()
