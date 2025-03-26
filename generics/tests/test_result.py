"""
Tests for the generic Result type.
"""

import unittest
import pytest
from generics.result import Result


class TestResult(unittest.TestCase):
    """Test cases for the Result type."""

    def test_ok_result(self) -> None:
        """Test creating and using Ok results."""
        # Test creating an Ok result
        result = Result.ok(42)
        self.assertTrue(result.is_ok())
        self.assertFalse(result.is_err())
        self.assertEqual(result.unwrap(), 42)

    def test_err_result(self) -> None:
        """Test creating and using Err results."""
        # Test creating an Err result
        result = Result.err("error")
        self.assertFalse(result.is_ok())
        self.assertTrue(result.is_err())
        self.assertEqual(result.unwrap_err(), "error")

    def test_unwrap_or(self) -> None:
        """Test unwrap_or with default values."""
        # Test unwrap_or with Ok result
        ok_result = Result.ok(42)
        self.assertEqual(ok_result.unwrap_or(0), 42)

        # Test unwrap_or with Err result
        err_result = Result.err("error")
        self.assertEqual(err_result.unwrap_or(0), 0)

    def test_map(self) -> None:
        """Test mapping over results."""
        # Test mapping over Ok result
        ok_result = Result.ok(2)
        mapped_ok = ok_result.map(lambda x: x * 2)
        self.assertTrue(mapped_ok.is_ok())
        self.assertEqual(mapped_ok.unwrap(), 4)

        # Test mapping over Err result
        err_result = Result.err("error")
        mapped_err = err_result.map(lambda x: x * 2)
        self.assertTrue(mapped_err.is_err())
        self.assertEqual(mapped_err.unwrap_err(), "error")

    def test_and_then(self) -> None:
        """Test chaining operations with and_then."""
        def safe_divide(x: float, y: float) -> Result[float, str]:
            if y == 0:
                return Result.err("division by zero")
            return Result.ok(x / y)

        # Test successful chain
        result = Result.ok(10).and_then(lambda x: safe_divide(x, 2))
        self.assertTrue(result.is_ok())
        self.assertEqual(result.unwrap(), 5.0)

        # Test failed chain
        result = Result.ok(10).and_then(lambda x: safe_divide(x, 0))
        self.assertTrue(result.is_err())
        self.assertEqual(result.unwrap_err(), "division by zero")

        # Test chain with initial error
        result = (
            Result.err("initial error")
            .and_then(lambda x: safe_divide(x, 2))
        )
        self.assertTrue(result.is_err())
        self.assertEqual(result.unwrap_err(), "initial error")

    def test_or_else(self) -> None:
        """Test error handling with or_else."""
        def handle_error(err: str) -> Result[int, str]:
            if "retry" in err:
                return Result.ok(42)
            return Result.err(f"unhandled: {err}")

        # Test successful recovery
        result = Result.err("please retry").or_else(handle_error)
        self.assertTrue(result.is_ok())
        self.assertEqual(result.unwrap(), 42)

        # Test failed recovery
        result = Result.err("fatal error").or_else(handle_error)
        self.assertTrue(result.is_err())
        self.assertEqual(result.unwrap_err(), "unhandled: fatal error")

        # Test or_else with Ok result
        result = Result.ok(123).or_else(handle_error)
        self.assertTrue(result.is_ok())
        self.assertEqual(result.unwrap(), 123)

    def test_unwrap_raises(self) -> None:
        """Test that unwrap raises on Err results."""
        with self.assertRaises(ValueError) as context:
            Result.err("error").unwrap()
        self.assertEqual(str(context.exception), "error")

    def test_unwrap_err_raises(self) -> None:
        """Test that unwrap_err raises on Ok results."""
        with self.assertRaises(ValueError) as context:
            Result.ok(42).unwrap_err()
        self.assertEqual(
            str(context.exception),
            "Called unwrap_err on Ok value: 42"
        )

    def test_map_err(self) -> None:
        """Test mapping over error values."""
        def add_context(err: str) -> str:
            return f"Error: {err}"

        # Test mapping over Err result
        result = Result.err("not found").map_err(add_context)
        self.assertTrue(result.is_err())
        self.assertEqual(result.unwrap_err(), "Error: not found")

        # Test mapping over Ok result
        result = Result.ok(42).map_err(add_context)
        self.assertTrue(result.is_ok())
        self.assertEqual(result.unwrap(), 42)

    def test_practical_example(self) -> None:
        """Test a practical example using Result."""
        def parse_int(s: str) -> Result[int, str]:
            try:
                return Result.ok(int(s))
            except ValueError:
                return Result.err(f"could not parse '{s}' as integer")

        def double(n: int) -> Result[int, str]:
            return Result.ok(n * 2)

        # Test successful chain
        result = parse_int("42").and_then(double)
        self.assertTrue(result.is_ok())
        self.assertEqual(result.unwrap(), 84)

        # Test failed parse
        result = parse_int("not a number").and_then(double)
        self.assertTrue(result.is_err())
        self.assertEqual(
            result.unwrap_err(),
            "could not parse 'not a number' as integer"
        )


if __name__ == "__main__":
    unittest.main()


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


def test_result_map_err() -> None:
    """Test mapping over Result errors."""

    def add_context(error: str) -> str:
        return f"Error occurred: {error}"

    assert (
        Result.err("bad input").map_err(add_context).unwrap_err()
        == "Error occurred: bad input"
    )
    assert Result.ok(42).map_err(add_context).unwrap() == 42


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
