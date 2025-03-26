# Generics in Python

This section demonstrates the use of generics in Python using type hints and the `typing` module. We'll explore various aspects of generic programming through practical examples.

## Diagram

```mermaid
classDiagram
    class Stack~T~ {
        -items: List[T]
        +push(item: T)
        +pop() T
        +peek() Optional[T]
        +is_empty() bool
        +size() int
    }
    class Result~T, E~ {
        +value: Optional[T]
        +error: Optional[E]
        +is_ok() bool
        +is_err() bool
        +unwrap() T
        +unwrap_err() E
    }
    class Repository~T~ {
        <<interface>>
        +find_by_id(id: str) Result[T, Error]
        +save(item: T) Result[T, Error]
        +delete(id: str) Result[None, Error]
    }
    class Cache~K, V~ {
        -items: Dict[K, V]
        -expiry: Dict[K, datetime]
        +get(key: K) Optional[V]
        +set(key: K, value: V)
        +has(key: K) bool
    }

    Stack --> "0..*" T : contains
    Result --> "0..1" T : success
    Result --> "0..1" E : failure
    Repository --> T : manages
    Cache --> K : indexes
    Cache --> V : stores
```

## Overview

Generics enable you to write flexible, reusable code that works with different types while maintaining type safety. Key benefits include:

- Type safety without code duplication
- Better IDE support and autocompletion
- Catch type-related errors at compile time
- Clear documentation of type requirements

## Implementation Details

We're implementing several generic types to demonstrate different aspects of generic programming:

1. **Stack[T]**: A generic stack data structure
   - Demonstrates basic generic class implementation
   - Shows type-safe operations on a collection
   - Implements standard container protocols

2. **Result[T, E]**: A type-safe error handling mechanism
   - Shows multiple type parameters
   - Implements the Railway-oriented programming pattern
   - Provides a functional approach to error handling

3. **Repository[T]**: A generic data access interface
   - Demonstrates generic protocols
   - Shows bounded type parameters
   - Implements the Repository pattern

4. **Cache[K, V]**: A generic key-value cache
   - Shows multiple type parameters with different roles
   - Implements time-based expiration
   - Demonstrates type constraints

## Example Usage

```python
# Stack Example
numbers = Stack[int]()
numbers.push(1)
numbers.push(2)
top = numbers.pop()  # type: int

# Result Example
def divide(a: float, b: float) -> Result[float, str]:
    if b == 0:
        return Result.err("Division by zero")
    return Result.ok(a / b)

result = divide(10, 2)
if result.is_ok():
    value = result.unwrap()  # type: float

# Repository Example
class UserRepo(Repository[User]):
    def find_by_id(self, id: str) -> Result[User, Error]:
        # Implementation
        pass

# Cache Example
cache = Cache[str, bytes](expiry=timedelta(minutes=5))
cache.set("key", b"value")
value = cache.get("key")  # type: Optional[bytes]
```

## Running the Examples

To run the demonstration:

```bash
python -m generics.main
```

## Running Tests

To run the tests with type checking:

```bash
python -m pytest --mypy
```

## Best Practices

1. **Type Variable Naming**
   - Use single uppercase letters (T, K, V) for simple type variables
   - Use descriptive names for complex types (Key, Value, Error)

2. **Constraints**
   - Use bounded type variables when operations require specific methods
   - Document type constraints in docstrings

3. **Error Handling**
   - Return Optional[T] when operations can fail
   - Use Result[T, E] for operations with error details

4. **Documentation**
   - Document type parameters in class and function docstrings
   - Include examples with type annotations

## Requirements

- Python 3.11+
- mypy
- pytest 