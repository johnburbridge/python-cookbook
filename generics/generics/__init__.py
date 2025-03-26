"""
Generic programming examples in Python.
"""

from .stack import Stack
from .result import Result
from .repository import Repository, InMemoryRepository, Identifiable, RepositoryError

__all__ = [
    "Stack",
    "Result",
    "Repository",
    "InMemoryRepository",
    "Identifiable",
    "RepositoryError",
]
