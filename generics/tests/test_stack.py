"""
Tests for the generic Stack implementation.
"""
import pytest
from typing import List
from generics.stack import Stack


def test_stack_creation() -> None:
    """Test stack creation with different types."""
    # Integer stack
    stack_int = Stack[int]()
    assert stack_int.is_empty()
    assert len(stack_int) == 0
    
    # String stack
    stack_str = Stack[str]()
    assert stack_str.is_empty()
    assert len(stack_str) == 0
    
    # List stack (stack of lists)
    stack_list = Stack[List[int]]()
    assert stack_list.is_empty()
    assert len(stack_list) == 0


def test_stack_push_pop() -> None:
    """Test pushing and popping items."""
    stack = Stack[int]()
    
    # Push items
    stack.push(1)
    assert not stack.is_empty()
    assert len(stack) == 1
    
    stack.push(2)
    assert len(stack) == 2
    
    # Pop items
    assert stack.pop() == 2
    assert len(stack) == 1
    
    assert stack.pop() == 1
    assert stack.is_empty()


def test_stack_peek() -> None:
    """Test peeking at the top item."""
    stack = Stack[str]()
    
    # Peek empty stack
    assert stack.peek() is None
    
    # Peek with items
    stack.push("first")
    assert stack.peek() == "first"
    
    stack.push("second")
    assert stack.peek() == "second"
    
    # Verify peek doesn't remove items
    assert len(stack) == 2


def test_stack_iteration() -> None:
    """Test iterating over stack items."""
    stack = Stack[int]()
    items = [1, 2, 3, 4, 5]
    
    # Push items
    for item in items:
        stack.push(item)
    
    # Verify iteration (should be in reverse order)
    assert list(stack) == list(reversed(items))


def test_stack_empty_pop() -> None:
    """Test popping from an empty stack raises IndexError."""
    stack = Stack[int]()
    
    with pytest.raises(IndexError):
        stack.pop()


def test_stack_type_safety() -> None:
    """Test type safety of the stack."""
    stack = Stack[int]()
    stack.push(42)
    
    # This would fail type checking:
    # stack.push("string")  # type: ignore
    
    # But this is fine:
    stack_str = Stack[str]()
    stack_str.push("string")


def test_stack_str_repr() -> None:
    """Test string representations of the stack."""
    stack = Stack[int]()
    stack.push(1)
    stack.push(2)
    
    assert str(stack) == "Stack([1, 2])"
    assert repr(stack) == "Stack[int]([1, 2])"


def test_complex_types() -> None:
    """Test stack with more complex types."""
    # Stack of lists
    stack_lists = Stack[List[int]]()
    stack_lists.push([1, 2, 3])
    stack_lists.push([4, 5, 6])
    
    assert stack_lists.pop() == [4, 5, 6]
    
    # Stack of tuples
    stack_tuples = Stack[tuple[str, int]]()
    stack_tuples.push(("answer", 42))
    
    assert stack_tuples.peek() == ("answer", 42) 