# Python Cookbook

[![CI](https://github.com/johnburbridge/python-cookbook/actions/workflows/ci.yml/badge.svg)](https://github.com/johnburbridge/python-cookbook/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/johnburbridge/python-cookbook/branch/main/graph/badge.svg)](https://codecov.io/gh/johnburbridge/python-cookbook)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains a collection of Python projects that exemplify common operations and design patterns in Python. It serves as a quick reference guide with practical examples (recipes) of how to implement frequently used libraries and design patterns in Python 3.11+.

## Development Setup

### Requirements
- Python 3.11+
- pip (Python package installer)

### Getting Started
1. Clone the repository
2. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

### Code Quality
This project uses several tools to maintain code quality:
- **black**: Code formatting
- **flake8**: Code linting
- **pytest**: Testing framework
- **pytest-cov**: Test coverage reporting

### Continuous Integration
The project uses GitHub Actions for CI, which runs on every push to main and pull requests:
- Runs tests against Python 3.11 and 3.12
- Enforces code formatting with black
- Runs linting with flake8
- Requires 70% test coverage
- Reports coverage to Codecov

## Recipes

### Design Patterns
- [x] [The Strategy Pattern](./strategy_pattern/README.md)
- [x] [The Factory Pattern](./factory_pattern/README.md)
- [x] [The Builder Pattern](./builder_pattern/README.md)
- [x] [The Observable Pattern](./observable_pattern/README.md)

### Beginner Topics
- [x] [Generics in Python](./generics/README.md)
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
