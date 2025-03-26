from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class Document(ABC):
    """
    The Document interface (Product) that defines operations all concrete document types must implement.
    This is the base class for all document types.
    """
    
    def __init__(self, title: str, author: str, content: str = ""):
        """
        Initialize a document with basic metadata.
        
        Args:
            title: The title of the document
            author: The author of the document
            content: The content of the document (default is empty string)
        """
        self.title = title
        self.author = author
        self.content = content
        self.metadata: Dict[str, Any] = {
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
        self.metadata[key] = value
    
    def get_metadata(self, key: str) -> Optional[Any]:
        """
        Get metadata from the document.
        
        Args:
            key: The metadata key
            
        Returns:
            Optional[Any]: The metadata value or None if the key doesn't exist
        """
        return self.metadata.get(key)
    
    @abstractmethod
    def generate(self) -> str:
        """
        Generate the document in its specific format.
        
        Returns:
            str: A string representation of the document
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