"""
Tests for the generic Result type.
"""
import pytest
from typing import List
from generics.result import Result


def test_result_creation() -> None:
    """Test Result creation with ok and err factory methods."""
    # Ok result
    ok_result: Result[int, str] = Result.ok(42)
    assert ok_result.is_ok()
    assert not ok_result.is_err()
    
    # Error result
    err_result: Result[int, str] = Result.err("error")
    assert err_result.is_err()
    assert not err_result.is_ok()


def test_result_invalid_creation() -> None:
    """Test that Result cannot be created with both value and error."""
    with pytest.raises(ValueError):
        Result(value=42, error="error")
    
    with pytest.raises(ValueError):
        Result()


def test_result_unwrap() -> None:
    """Test unwrapping Result values."""
    # Unwrap ok
    ok_result = Result.ok(42)
    assert ok_result.unwrap() == 42
    
    # Unwrap error should raise
    err_result = Result.err("error")
    with pytest.raises(ValueError):
        err_result.unwrap()


def test_result_unwrap_err() -> None:
    """Test unwrapping Result errors."""
    # Unwrap error
    err_result = Result.err("error")
    assert err_result.unwrap_err() == "error"
    
    # Unwrap ok should raise
    ok_result = Result.ok(42)
    with pytest.raises(ValueError):
        ok_result.unwrap_err()


def test_result_unwrap_or() -> None:
    """Test unwrap_or with default values."""
    assert Result.ok(42).unwrap_or(0) == 42
    assert Result.err("error").unwrap_or(0) == 0


def test_result_unwrap_or_else() -> None:
    """Test unwrap_or_else with mapping function."""
    def handle_error(error: str) -> int:
        return len(error)
    
    assert Result.ok(42).unwrap_or_else(handle_error) == 42
    assert Result.err("error").unwrap_or_else(handle_error) == 5


def test_result_expect() -> None:
    """Test expect with custom messages."""
    assert Result.ok(42).expect("should be ok") == 42
    
    with pytest.raises(ValueError) as exc_info:
        Result.err("error").expect("custom message")
    assert str(exc_info.value) == "custom message: error"


def test_result_expect_err() -> None:
    """Test expect_err with custom messages."""
    assert Result.err("error").expect_err("should be error") == "error"
    
    with pytest.raises(ValueError) as exc_info:
        Result.ok(42).expect_err("custom message")
    assert str(exc_info.value) == "custom message: 42"


def test_result_map() -> None:
    """Test mapping over Result values."""
    def square(x: int) -> int:
        return x * x
    
    assert Result.ok(6).map(square).unwrap() == 36
    assert Result.err("error").map(square).unwrap_err() == "error"


def test_result_map_err() -> None:
    """Test mapping over Result errors."""
    def add_context(error: str) -> str:
        return f"Error occurred: {error}"
    
    assert Result.err("bad input").map_err(add_context).unwrap_err() == "Error occurred: bad input"
    assert Result.ok(42).map_err(add_context).unwrap() == 42


def test_result_and_then() -> None:
    """Test chaining Result operations."""
    def divide(a: float, b: float) -> Result[float, str]:
        if b == 0:
            return Result.err("division by zero")
        return Result.ok(a / b)
    
    def reciprocal(x: float) -> Result[float, str]:
        return divide(1.0, x)
    
    # Chain successful operations
    assert Result.ok(2.0).and_then(reciprocal).unwrap() == 0.5
    
    # Chain with error
    assert Result.ok(0.0).and_then(reciprocal).unwrap_err() == "division by zero"
    
    # Chain after error
    assert Result.err("error").and_then(reciprocal).unwrap_err() == "error"


def test_practical_example() -> None:
    """Test a practical example using Result."""
    def parse_number(s: str) -> Result[int, str]:
        try:
            return Result.ok(int(s))
        except ValueError:
            return Result.err(f"could not parse '{s}' as integer")
    
    def double(x: int) -> Result[int, str]:
        return Result.ok(x * 2)
    
    # Successful chain
    result = parse_number("21").and_then(double)
    assert result.unwrap() == 42
    
    # Error chain
    result = parse_number("not a number").and_then(double)
    assert result.unwrap_err() == "could not parse 'not a number' as integer" 