"""
Generic Repository Interface

This module demonstrates the use of generic protocols and bounded type parameters
through a Repository pattern implementation.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol, TypeVar, Generic, Dict, List, Any, Hashable
from .result import Result


class Unit:
    """Represents a void or no-value return type."""

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Unit)

    def __repr__(self) -> str:
        return "Unit"


# ID must be hashable to be used as a dictionary key
ID = TypeVar("ID", bound=Hashable)


class Identifiable(Protocol[ID]):
    """Protocol for objects that can be stored in a repository."""

    @property
    def id(self) -> ID:
        """Get the unique identifier of the object."""
        ...


# T must implement the Identifiable protocol with the same ID type
T = TypeVar("T", bound="Identifiable[Any]")


@dataclass
class RepositoryError:
    """Represents errors that can occur in repository operations."""

    message: str
    code: str

    @classmethod
    def not_found(cls, id: Any) -> "RepositoryError":
        """Create a not found error."""
        return cls(f"Entity with id '{id}' not found", "NOT_FOUND")

    @classmethod
    def already_exists(cls, id: Any) -> "RepositoryError":
        """Create an already exists error."""
        return cls(f"Entity with id '{id}' already exists", "ALREADY_EXISTS")

    @classmethod
    def validation_error(cls, message: str) -> "RepositoryError":
        """Create a validation error."""
        return cls(message, "VALIDATION_ERROR")


class Repository(Generic[T, ID], ABC):
    """
    Generic repository interface for storing and retrieving objects.

    Type Parameters:
        T: The type of objects stored in the repository.
           Must implement the Identifiable protocol.
        ID: The type of the identifier used by the entities.
           Must be hashable.

    Examples:
        >>> @dataclass
        ... class User:
        ...     id: int  # Using integer IDs
        ...     name: str
        ...
        >>> class UserRepository(Repository[User, int]):
        ...     def __init__(self):
        ...         self._users: Dict[int, User] = {}
        ...
        ...     def find_by_id(self, id: int) -> Result[User, RepositoryError]:
        ...         if user := self._users.get(id):
        ...             return Result.ok(user)
        ...         return Result.err(RepositoryError.not_found(id))
        ...
        >>> from uuid import UUID
        >>> @dataclass
        ... class Post:
        ...     id: UUID  # Using UUID for IDs
        ...     title: str
        ...
        >>> class PostRepository(Repository[Post, UUID]):
        ...     # Implementation with UUID keys
        ...     pass
    """

    @abstractmethod
    def find_by_id(self, id: ID) -> "Result[T, RepositoryError]":
        """
        Find an entity by its ID.

        Args:
            id: The ID of the entity to find.

        Returns:
            Result containing either the found entity or an error.
        """
        ...

    @abstractmethod
    def find_all(self) -> "Result[List[T], RepositoryError]":
        """
        Find all entities in the repository.

        Returns:
            Result containing either a list of all entities or an error.
        """
        ...

    @abstractmethod
    def save(self, entity: T) -> "Result[T, RepositoryError]":
        """
        Save an entity to the repository.

        Args:
            entity: The entity to save.

        Returns:
            Result containing either the saved entity or an error.
        """
        ...

    @abstractmethod
    def delete(self, id: ID) -> "Result[Unit, RepositoryError]":
        """
        Delete an entity from the repository.

        Args:
            id: The ID of the entity to delete.

        Returns:
            Result indicating success or an error.
        """
        ...


class InMemoryRepository(Repository[T, ID]):
    """
    In-memory implementation of the Repository interface.

    This class provides a simple dictionary-based storage implementation
    for testing and demonstration purposes.

    Type Parameters:
        T: The type of objects stored in the repository.
        ID: The type of the identifier used by the entities.
    """

    def __init__(self) -> None:
        """Initialize an empty repository."""
        self._items: Dict[ID, T] = {}

    def find_by_id(self, id: ID) -> "Result[T, RepositoryError]":
        if item := self._items.get(id):
            return Result.ok(item)
        return Result.err(RepositoryError.not_found(id))

    def find_all(self) -> "Result[List[T], RepositoryError]":
        return Result.ok(list(self._items.values()))

    def save(self, entity: T) -> "Result[T, RepositoryError]":
        if entity.id in self._items:
            return Result.err(RepositoryError.already_exists(entity.id))
        self._items[entity.id] = entity
        return Result.ok(entity)

    def delete(self, id: ID) -> "Result[Unit, RepositoryError]":
        if id not in self._items:
            return Result.err(RepositoryError.not_found(id))
        del self._items[id]
        return Result.ok(Unit())
