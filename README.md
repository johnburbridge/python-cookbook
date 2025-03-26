# Python Cookbook

This repository contains a collection of Python projects that exemplify common operations and design patterns in Python. It serves as a quick reference guide with practical examples (recipes) of how to implement frequently used libraries and design patterns in Python 3.11+.

## Recipes

### Design Patterns
1. [The Strategy Pattern](./strategy_pattern/README.md) - Implemented
2. [The Factory Pattern](./factory_pattern/README.md) - Implemented
3. [The Builder Pattern](./builder_pattern/README.md) - Implemented
4. [The Observable Pattern](./observable_pattern/README.md) - Implemented

### Beginner Topics
5. Generics in Python
6. Reading and writing JSON
7. Reading and writing YAML
8. Handling HTTP Requests
9. Data classes
10. Error Handling and Logging
11. Context Managers (with statement)
12. Decorators

### Intermediate Topics
13. Reading and writing from/to Postgres
14. Reading and writing from/to MongoDB
15. Reading and writing from/to Redis
16. Type Hinting and Static Type Checking
17. Functional Programming
18. Packaging and Distribution
19. API Development with FastAPI
20. Concurrent Processing (Threading vs Multiprocessing)
21. Property-Based Testing
22. Event-Driven Programming

### Advanced Topics
23. Asynchronous Programming (asyncio)
24. Metaprogramming
25. Performance Optimization
26. Memory Management
27. Cython Integration

## Project Structure

Each recipe follows a consistent structure:

```
.
├── <pattern_name>/
│   ├── README.md
│   ├── <pattern_name>/
│   ├── tests/
│   ├── main.py
│   └── requirements.txt
```

Where:
- README.md contains detailed notes about the recipe, including implementation details and usage examples
- main.py provides a demonstration of the pattern in action
- tests/ contains unit tests that validate the implementation
