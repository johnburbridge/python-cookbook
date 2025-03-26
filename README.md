# Python Cookbook

This repository contains a collection of Python projects that exemplify common operations and design patterns in Python. It serves as a quick reference guide with practical examples (recipes) of how to implement frequently used libraries and design patterns in Python 3.11+.

## Recipes

### Design Patterns
- [x] [The Strategy Pattern](./strategy_pattern/README.md)
- [x] [The Factory Pattern](./factory_pattern/README.md)
- [x] [The Builder Pattern](./builder_pattern/README.md)
- [x] [The Observable Pattern](./observable_pattern/README.md)

### Beginner Topics
- [ ] Generics in Python
- [ ] Reading and writing JSON
- [ ] Reading and writing YAML
- [ ] Handling HTTP Requests
- [ ] Data classes
- [ ] Error Handling and Logging
- [ ] Context Managers (with statement)
- [ ] Decorators

### Intermediate Topics
- [ ] Reading and writing from/to Postgres
- [ ] Reading and writing from/to MongoDB
- [ ] Reading and writing from/to Redis
- [ ] Type Hinting and Static Type Checking
- [ ] Functional Programming
- [ ] Packaging and Distribution
- [ ] API Development with FastAPI
- [ ] Concurrent Processing (Threading vs Multiprocessing)
- [ ] Property-Based Testing
- [ ] Event-Driven Programming

### Advanced Topics
- [ ] Asynchronous Programming (asyncio)
- [ ] Metaprogramming
- [ ] Performance Optimization
- [ ] Memory Management
- [ ] Cython Integration

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
