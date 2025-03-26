# Strategy Pattern

The Strategy Pattern is a behavioral design pattern that enables selecting an algorithm at runtime. Instead of implementing a single algorithm directly, code receives run-time instructions as to which algorithm to use.

## Key Components

1. **Strategy Interface**: Declares an interface common to all supported algorithms.
2. **Concrete Strategies**: Implement the algorithm using the strategy interface.
3. **Context**: Maintains a reference to a Strategy object and is configured with a ConcreteStrategy object.

## Benefits

- Encapsulates algorithms in separate classes
- Makes it easy to switch between different algorithms
- Eliminates conditional statements
- Enables the behavior of an object to change at runtime
- Promotes the open/closed principle (open for extension, closed for modification)

## Example

In this example, we implement different payment methods (credit card, PayPal, and Bitcoin) as strategies for an online shopping cart.

## Further Reading

- [Refactoring Guru - Strategy Pattern](https://refactoring.guru/design-patterns/strategy)
- [Python 3 Patterns, Recipes and Idioms - Strategy Pattern](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/FunctionObjects.html)
- [Real Python - The Strategy Pattern in Python](https://realpython.com/strategy-pattern-python/) 