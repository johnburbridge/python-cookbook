"""
Generic Result Type

This module implements a Result type for type-safe error handling,
similar to Rust's Result type.
"""
from typing import TypeVar, Generic, Optional, Callable, Any
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
    _has_value: bool
    
    def __init__(self, value: Optional[T] = None, error: Optional[E] = None) -> None:
        """Initialize a Result with either a value or an error."""
        if error is not None and value is not None:
            raise ValueError("Result cannot have both a value and an error")
        if error is None and value is None:
            raise ValueError("Result must have either a value or an error")
        self._value = value
        self._error = error
        self._has_value = error is None
    
    @classmethod
    def ok(cls, value: T) -> 'Result[T, Any]':
        """Create a successful Result with a value."""
        return cls(value=value)
    
    @classmethod
    def err(cls, error: E) -> 'Result[Any, E]':
        """Create a failed Result with an error."""
        return cls(error=error)
    
    def is_ok(self) -> bool:
        """Check if the Result contains a success value."""
        return self._has_value
    
    def is_err(self) -> bool:
        """Check if the Result contains an error."""
        return not self._has_value
    
    def unwrap(self) -> T:
        """Get the success value, raising an error if not successful."""
        if not self._has_value:
            raise ValueError(f"Called unwrap on an error Result: {self._error}")
        return self._value  # type: ignore
    
    def unwrap_err(self) -> E:
        """Get the error value, raising an error if successful."""
        if self._has_value:
            raise ValueError("Called unwrap_err on an ok Result")
        return self._error  # type: ignore
    
    def unwrap_or(self, default: T) -> T:
        """Get the success value or a default if error."""
        return self._value if self._has_value else default  # type: ignore
    
    def unwrap_or_else(self, op: Callable[[E], T]) -> T:
        """Get the success value or compute it from the error."""
        return self._value if self._has_value else op(self._error)  # type: ignore
    
    def expect(self, msg: str) -> T:
        """Get the success value or raise an error with a custom message."""
        if not self._has_value:
            raise ValueError(f"{msg}: {self._error}")
        return self._value  # type: ignore
    
    def expect_err(self, msg: str) -> E:
        """Get the error value or raise an error with a custom message."""
        if self._has_value:
            raise ValueError(f"{msg}: {self._value}")
        return self._error  # type: ignore
    
    def map(self, op: Callable[[T], T]) -> 'Result[T, E]':
        """Apply a function to the success value if present."""
        if not self._has_value:
            return Result(error=self._error)
        return Result(value=op(self._value))  # type: ignore
    
    def map_err(self, op: Callable[[E], E]) -> 'Result[T, E]':
        """Apply a function to the error value if present."""
        if self._has_value:
            return Result(value=self._value)
        return Result(error=op(self._error))  # type: ignore
    
    def and_then(self, op: Callable[[T], 'Result[T, E]']) -> 'Result[T, E]':
        """Chain operations that might fail."""
        if not self._has_value:
            return Result(error=self._error)
        return op(self._value)  # type: ignore
    
    def __str__(self) -> str:
        """Get a string representation of the Result."""
        if not self._has_value:
            return f"Err({self._error})"
        return f"Ok({self._value})"
    
    def __repr__(self) -> str:
        """Get a detailed string representation of the Result."""
        if not self._has_value:
            return f"Result.err({self._error!r})"
        return f"Result.ok({self._value!r})" 