"""
Example usage of generic types in Python.
"""

from dataclasses import dataclass, field
from typing import List
from generics.stack import Stack
from generics.result import Result, Ok, Err
from generics.repository import (
    Repository,
    InMemoryRepository,
    Identifiable,
    RepositoryError,
)
from uuid import uuid4


def demonstrate_stack() -> None:
    """Demonstrate the generic Stack type."""
    print("\n=== Stack Examples ===")

    # Example 1: Stack of integers
    print("\nStack of integers:")
    int_stack = Stack[int]()
    int_stack.push(1)
    int_stack.push(2)
    int_stack.push(3)
    print(f"Stack contents: {int_stack}")
    print(f"Popped value: {int_stack.pop()}")
    print(f"Current top value: {int_stack.peek()}")

    # Example 2: Stack of strings
    print("\nStack of strings:")
    str_stack = Stack[str]()
    str_stack.push("hello")
    str_stack.push("world")
    print(f"Stack contents: {str_stack}")
    print("Iterating over stack:")
    for item in str_stack:
        print(f"  {item}")

    # Example 3: Stack of lists
    print("\nStack of lists:")
    list_stack = Stack[List[int]]()
    list_stack.push([1, 2, 3])
    list_stack.push([4, 5, 6])
    print(f"Stack contents: {list_stack}")
    top_list = list_stack.pop()
    print(f"Popped list: {top_list}")


def demonstrate_result() -> None:
    """Demonstrate the generic Result type."""
    print("\n=== Result Examples ===")

    # Example 1: Division with error handling
    print("\nDivision examples:")

    def divide(a: float, b: float) -> Result[float, str]:
        if b == 0:
            return Result.err("division by zero")
        return Result.ok(a / b)

    result1 = divide(10, 2)
    result2 = divide(10, 0)
    result3 = divide(10, 2)

    print(f"Result 1: {result1.unwrap()}")
    print(f"Result 2: Error - {result2.unwrap_err()}")
    print(f"Result 3: {result3.unwrap_or(0.0)}")

    # Example 2: Chaining operations
    print("\nChaining operations:")

    def parse_int(s: str) -> Result[int, str]:
        try:
            return Result.ok(int(s))
        except ValueError:
            return Result.err(f"could not parse '{s}' as integer")

    def double(n: int) -> Result[int, str]:
        return Result.ok(n * 2)

    result = parse_int("42").and_then(double)
    print(f"Double of 42: {result.unwrap()}")

    result = parse_int("not a number").and_then(double)
    print(f"Error processing not a number: {result.unwrap_err()}")

    result = parse_int("21").and_then(double)
    print(f"Double of 21: {result.unwrap()}")

    # Example 3: Mapping and defaults
    print("\nMapping and defaults:")

    def square_number(s: str) -> Result[int, str]:
        return parse_int(s).map(lambda x: x * x)

    numbers = ["123", "456", "abc", "789"]
    for num in numbers:
        result = square_number(num)
        print(f"Square of {num}: {result.unwrap_or(0)}")


def demonstrate_repository() -> None:
    """Demonstrate the generic Repository type."""
    print("\n=== Repository Examples ===")

    @dataclass
    class User:
        """Example user entity."""

        _id: str = field(repr=False)
        name: str
        email: str

        @property
        def id(self) -> str:
            """Get the user's ID."""
            return self._id

    # Create a repository for User entities with string IDs
    user_repo: Repository[User, str] = InMemoryRepository[User, str]()

    # Example 1: Basic CRUD operations
    print("\nBasic CRUD operations:")

    # Create
    user = User(_id="1", name="John Doe", email="john@example.com")
    result = user_repo.save(user)
    if result.is_ok():
        print(f"Created user: {result.unwrap()}")

    # Read
    result = user_repo.find_by_id("1")
    if result.is_ok():
        print(f"Found user: {result.unwrap()}")

    # Update (in our simple implementation, this is a save)
    updated_user = User(_id="1", name="John Doe", email="john.doe@example.com")
    user_repo.delete("1")  # Delete first since our implementation doesn't update
    result = user_repo.save(updated_user)
    if result.is_ok():
        print(f"Updated user: {result.unwrap()}")

    # Delete
    result = user_repo.delete("1")
    if result.is_ok():
        print("Deleted user successfully")

    # Example 2: Error handling
    print("\nError handling:")

    # Try to find non-existent user
    result = user_repo.find_by_id("999")
    if result.is_err():
        error = result.unwrap_err()
        print(f"Error finding user: {error.message} (Code: {error.code})")

    # Try to save duplicate user
    user1 = User(_id="2", name="Jane Doe", email="jane@example.com")
    user2 = User(_id="2", name="Different Name", email="different@example.com")

    user_repo.save(user1)
    result = user_repo.save(user2)
    if result.is_err():
        error = result.unwrap_err()
        print(f"Error saving duplicate user: {error.message} (Code: {error.code})")

    # Example 3: Working with multiple types
    print("\nMultiple entity types:")

    @dataclass
    class Post:
        """Example post entity."""

        _id: str = field(repr=False)
        title: str
        content: str
        author_id: str

        @property
        def id(self) -> str:
            """Get the post's ID."""
            return self._id

    # Create a separate repository for Post entities with string IDs
    post_repo: Repository[Post, str] = InMemoryRepository[Post, str]()

    # Create a post
    post = Post(
        _id="1", title="Hello World", content="This is my first post", author_id="2"
    )
    result = post_repo.save(post)
    if result.is_ok():
        print(f"Created post: {result.unwrap()}")

    # Find all posts
    result = post_repo.find_all()
    if result.is_ok():
        posts = result.unwrap()
        print(f"Found {len(posts)} posts")


def main() -> None:
    """Run all generic type demonstrations."""
    demonstrate_stack()
    demonstrate_result()
    demonstrate_repository()


if __name__ == "__main__":
    main()
