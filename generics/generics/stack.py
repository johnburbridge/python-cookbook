"""
Generic Stack Implementation

This module demonstrates the use of generics in Python by implementing
a type-safe stack data structure.
"""
from typing import TypeVar, Generic, List, Optional
from collections.abc import Iterator


T = TypeVar('T')

class Stack(Generic[T]):
    """
    A generic stack implementation that can hold elements of any type T.
    
    Type Parameters:
        T: The type of elements stored in the stack.
    
    Examples:
        >>> stack = Stack[int]()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.pop()
        2
        >>> stack.peek()
        1
    """
    
    def __init__(self) -> None:
        """Initialize an empty stack."""
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        """
        Push an item onto the stack.
        
        Args:
            item: The item to push onto the stack.
        """
        self._items.append(item)
    
    def pop(self) -> T:
        """
        Remove and return the top item from the stack.
        
        Returns:
            The item at the top of the stack.
            
        Raises:
            IndexError: If the stack is empty.
        """
        if not self._items:
            raise IndexError("Pop from empty stack")
        return self._items.pop()
    
    def peek(self) -> Optional[T]:
        """
        Return the top item from the stack without removing it.
        
        Returns:
            The item at the top of the stack, or None if the stack is empty.
        """
        if not self._items:
            return None
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """
        Check if the stack is empty.
        
        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self._items) == 0
    
    def size(self) -> int:
        """
        Get the number of items in the stack.
        
        Returns:
            The number of items in the stack.
        """
        return len(self._items)
    
    def __iter__(self) -> Iterator[T]:
        """
        Return an iterator over the stack's items (from top to bottom).
        
        Returns:
            An iterator over the stack's items.
        """
        return reversed(self._items)
    
    def __len__(self) -> int:
        """
        Get the number of items in the stack.
        
        Returns:
            The number of items in the stack.
        """
        return len(self._items)
    
    def __str__(self) -> str:
        """
        Return a string representation of the stack.
        
        Returns:
            A string representation of the stack.
        """
        return f"Stack({self._items})"
    
    def __repr__(self) -> str:
        """
        Return a detailed string representation of the stack.
        
        Returns:
            A detailed string representation of the stack.
        """
        type_name = self._items.__class__.__name__
        if type_name == "list":
            # Get the type argument from the first item if available
            if self._items:
                type_name = self._items[0].__class__.__name__
        return f"Stack[{type_name}]({self._items})" 