"""
Tests for the generic Repository implementation.
"""
from dataclasses import dataclass, field
import pytest
from typing import List
from generics.repository import Repository, InMemoryRepository, RepositoryError, Identifiable, Unit
from generics.result import Result
from uuid import UUID, uuid4


@dataclass(frozen=True)
class User:
    """Example user entity with string ID."""
    _id: str = field(repr=False)
    name: str
    email: str

    @property
    def id(self) -> str:
        """Get the user's ID."""
        return self._id


@dataclass(frozen=True)
class Post:
    """Example post entity with UUID ID."""
    _id: UUID = field(repr=False)
    title: str
    content: str

    @property
    def id(self) -> UUID:
        """Get the post's ID."""
        return self._id


@dataclass(frozen=True)
class Counter:
    """Example counter entity with integer ID."""
    _id: int = field(repr=False)
    value: int

    @property
    def id(self) -> int:
        """Get the counter's ID."""
        return self._id


def test_repository_with_string_id() -> None:
    """Test repository operations with string IDs."""
    repo: Repository[User, str] = InMemoryRepository[User, str]()
    user = User(_id="user-1", name="John Doe", email="john@example.com")
    
    # Save
    result = repo.save(user)
    assert result.is_ok()
    assert result.unwrap() == user
    
    # Find
    result = repo.find_by_id("user-1")
    assert result.is_ok()
    assert result.unwrap() == user
    
    # Delete
    result = repo.delete("user-1")
    assert result.is_ok()
    assert result.unwrap() == Unit()


def test_repository_with_uuid() -> None:
    """Test repository operations with UUID IDs."""
    repo: Repository[Post, UUID] = InMemoryRepository[Post, UUID]()
    post_id = uuid4()
    post = Post(_id=post_id, title="Hello", content="World")
    
    # Save
    result = repo.save(post)
    assert result.is_ok()
    assert result.unwrap() == post
    
    # Find
    result = repo.find_by_id(post_id)
    assert result.is_ok()
    assert result.unwrap() == post
    
    # Not found with different UUID
    result = repo.find_by_id(uuid4())
    assert result.is_err()
    assert result.unwrap_err().code == "NOT_FOUND"


def test_repository_with_int_id() -> None:
    """Test repository operations with integer IDs."""
    repo: Repository[Counter, int] = InMemoryRepository[Counter, int]()
    counter = Counter(_id=1, value=42)
    
    # Save
    result = repo.save(counter)
    assert result.is_ok()
    assert result.unwrap() == counter
    
    # Find
    result = repo.find_by_id(1)
    assert result.is_ok()
    assert result.unwrap() == counter
    
    # Update value
    new_counter = Counter(_id=1, value=43)
    repo.delete(1)
    result = repo.save(new_counter)
    assert result.is_ok()
    assert result.unwrap().value == 43


def test_repository_find_all() -> None:
    """Test finding all entities."""
    repo: Repository[User, str] = InMemoryRepository[User, str]()
    users = [
        User(_id="1", name="John Doe", email="john@example.com"),
        User(_id="2", name="Jane Doe", email="jane@example.com")
    ]
    
    for user in users:
        repo.save(user)
    
    result = repo.find_all()
    assert result.is_ok()
    assert set(result.unwrap()) == set(users)


def test_repository_error_messages() -> None:
    """Test error messages from the repository."""
    repo: Repository[User, str] = InMemoryRepository[User, str]()
    
    # Test not found error
    result = repo.find_by_id("999")
    assert result.is_err()
    error = result.unwrap_err()
    assert error.code == "NOT_FOUND"
    assert "999" in error.message
    
    # Test already exists error
    user = User(_id="1", name="John Doe", email="john@example.com")
    repo.save(user)
    result = repo.save(user)
    assert result.is_err()
    error = result.unwrap_err()
    assert error.code == "ALREADY_EXISTS"
    assert "1" in error.message


def test_practical_example() -> None:
    """Test a practical example using the repository."""
    # Use UUID for post IDs
    repo: Repository[Post, UUID] = InMemoryRepository[Post, UUID]()
    
    def create_post(title: str, content: str) -> Result[Post, RepositoryError]:
        """Create a new post with validation."""
        if len(title) < 3:
            return Result.err(RepositoryError(
                code="VALIDATION_ERROR",
                message="Title must be at least 3 characters long"
            ))
        
        post = Post(_id=uuid4(), title=title, content=content)
        return repo.save(post)
    
    def update_content(post_id: UUID, new_content: str) -> Result[Post, RepositoryError]:
        """Update a post's content."""
        # Find post
        post_result = repo.find_by_id(post_id)
        if post_result.is_err():
            return post_result
        
        # Update and save
        post = post_result.unwrap()
        updated_post = Post(_id=post.id, title=post.title, content=new_content)
        delete_result = repo.delete(post_id)
        if delete_result.is_err():
            return Result.err(delete_result.unwrap_err())
        return repo.save(updated_post)
    
    # Test post creation
    result = create_post("Hello World", "Initial content")
    assert result.is_ok()
    post = result.unwrap()
    
    # Test invalid title
    result = create_post("Hi", "Too short title")
    assert result.is_err()
    error = result.unwrap_err()
    assert error.code == "VALIDATION_ERROR"
    
    # Test content update
    result = update_content(post.id, "Updated content")
    assert result.is_ok()
    updated = result.unwrap()
    assert updated.content == "Updated content"
    assert updated.title == "Hello World"  # Title unchanged 