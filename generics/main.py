"""
Example usage of generic types in Python.
"""
from typing import List
from generics import Stack
from generics.result import Result


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
    def divide(a: float, b: float) -> Result[float, str]:
        """Divide two numbers, returning an error if dividing by zero."""
        if b == 0:
            return Result.err("division by zero")
        return Result.ok(a / b)
    
    print("\nDivision examples:")
    results = [
        divide(10, 2),
        divide(1, 0),
        divide(15, 3)
    ]
    
    for i, result in enumerate(results, 1):
        if result.is_ok():
            print(f"Result {i}: {result.unwrap()}")
        else:
            print(f"Result {i}: Error - {result.unwrap_err()}")
    
    # Example 2: Chaining operations
    def parse_number(s: str) -> Result[int, str]:
        """Parse a string to an integer."""
        try:
            return Result.ok(int(s))
        except ValueError:
            return Result.err(f"could not parse '{s}' as integer")
    
    def double(x: int) -> Result[int, str]:
        """Double a number."""
        return Result.ok(x * 2)
    
    print("\nChaining operations:")
    inputs = ["42", "not a number", "21"]
    
    for s in inputs:
        # Chain parse_number and double operations
        result = parse_number(s).and_then(double)
        if result.is_ok():
            print(f"Double of {s}: {result.unwrap()}")
        else:
            print(f"Error processing {s}: {result.unwrap_err()}")
    
    # Example 3: Using map and unwrap_or
    print("\nMapping and defaults:")
    numbers = ["123", "456", "abc", "789"]
    
    for num in numbers:
        # Try to parse and square the number, or use 0 if it fails
        result = (parse_number(num)
                 .map(lambda x: x * x)
                 .unwrap_or(0))
        print(f"Square of {num}: {result}")


def main() -> None:
    """Run all generic type demonstrations."""
    demonstrate_stack()
    demonstrate_result()


if __name__ == "__main__":
    main() 