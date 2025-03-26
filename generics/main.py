"""
Example usage of generic types in Python.
"""
from typing import List
from generics import Stack


def main() -> None:
    # Example 1: Stack of integers
    print("Stack of integers:")
    int_stack = Stack[int]()
    int_stack.push(1)
    int_stack.push(2)
    int_stack.push(3)
    print(f"Stack contents: {int_stack}")
    print(f"Popped value: {int_stack.pop()}")
    print(f"Current top value: {int_stack.peek()}")
    print()

    # Example 2: Stack of strings
    print("Stack of strings:")
    str_stack = Stack[str]()
    str_stack.push("hello")
    str_stack.push("world")
    print(f"Stack contents: {str_stack}")
    print(f"Iterating over stack:")
    for item in str_stack:
        print(f"  {item}")
    print()

    # Example 3: Stack of lists
    print("Stack of lists:")
    list_stack = Stack[List[int]]()
    list_stack.push([1, 2, 3])
    list_stack.push([4, 5, 6])
    print(f"Stack contents: {list_stack}")
    top_list = list_stack.pop()
    print(f"Popped list: {top_list}")
    print()

    # Example 4: Stack of tuples
    print("Stack of tuples:")
    tuple_stack = Stack[tuple[str, int]]()
    tuple_stack.push(("answer", 42))
    tuple_stack.push(("pi", 314))
    print(f"Stack contents: {tuple_stack}")
    print(f"Stack size: {len(tuple_stack)}")


if __name__ == "__main__":
    main() 