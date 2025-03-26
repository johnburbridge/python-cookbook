"""
Generic Result Type

This module implements a Result type for type-safe error handling,
similar to Rust's Result type.
"""
from typing import TypeVar, Generic, Optional, Callable, NoReturn
from dataclasses import dataclass


T = TypeVar('T')  # Success type
E = TypeVar('E')  # Error type


@dataclass
class Result(Generic[T, E]):
    """
    A type that represents either success (Ok) or failure (Err).
    
    Type Parameters:
        T: The type of the success value
        E: The type of the error value
    
    Examples:
        >>> def divide(a: float, b: float) -> Result[float, str]:
        ...     if b == 0:
        ...         return Result.err("Division by zero")
        ...     return Result.ok(a / b)
        ...
        >>> result = divide(10, 2)
        >>> if result.is_ok():
        ...     value = result.unwrap()  # type: float
        >>> result = divide(1, 0)
        >>> if result.is_err():
        ...     error = result.unwrap_err()  # type: str
    """
    
    _value: Optional[T]
    _error: Optional[E]
    
    def __init__(self, value: Optional[T] = None, error: Optional[E] = None) -> None:
        """Initialize a Result with either a value or an error."""
        if (value is not None and error is not None) or (value is None and error is None):
            raise ValueError("Result must have either a value or an error, not both or neither")
        self._value = value
        self._error = error
    
    @classmethod
    def ok(cls, value: T) -> 'Result[T, E]':
        """Create a successful Result with a value."""
        return cls(value=value)
    
    @classmethod
    def err(cls, error: E) -> 'Result[T, E]':
        """Create a failed Result with an error."""
        return cls(error=error)
    
    def is_ok(self) -> bool:
        """Check if the Result is successful."""
        return self._value is not None
    
    def is_err(self) -> bool:
        """Check if the Result is a failure."""
        return self._error is not None
    
    def unwrap(self) -> T:
        """
        Get the success value.
        
        Raises:
            ValueError: If the Result is an error.
        """
        if self._value is None:
            raise ValueError(f"Cannot unwrap error result: {self._error}")
        return self._value
    
    def unwrap_err(self) -> E:
        """
        Get the error value.
        
        Raises:
            ValueError: If the Result is successful.
        """
        if self._error is None:
            raise ValueError(f"Cannot unwrap ok result: {self._value}")
        return self._error
    
    def unwrap_or(self, default: T) -> T:
        """Get the success value or a default if it's an error."""
        return self._value if self._value is not None else default
    
    def unwrap_or_else(self, op: Callable[[E], T]) -> T:
        """Get the success value or compute it from the error."""
        return self._value if self._value is not None else op(self._error)  # type: ignore
    
    def expect(self, msg: str) -> T:
        """
        Get the success value or raise an error with a custom message.
        
        Args:
            msg: The error message to use if the Result is an error.
            
        Raises:
            ValueError: If the Result is an error.
        """
        if self._value is None:
            raise ValueError(f"{msg}: {self._error}")
        return self._value
    
    def expect_err(self, msg: str) -> E:
        """
        Get the error value or raise an error with a custom message.
        
        Args:
            msg: The error message to use if the Result is successful.
            
        Raises:
            ValueError: If the Result is successful.
        """
        if self._error is None:
            raise ValueError(f"{msg}: {self._value}")
        return self._error
    
    def map(self, op: Callable[[T], T]) -> 'Result[T, E]':
        """Apply a function to the success value if present."""
        if self._value is not None:
            return Result.ok(op(self._value))
        return Result(error=self._error)
    
    def map_err(self, op: Callable[[E], E]) -> 'Result[T, E]':
        """Apply a function to the error value if present."""
        if self._error is not None:
            return Result(error=op(self._error))
        return Result(value=self._value)
    
    def and_then(self, op: Callable[[T], 'Result[T, E]']) -> 'Result[T, E]':
        """Chain operations that might fail."""
        if self._value is not None:
            return op(self._value)
        return Result(error=self._error) 