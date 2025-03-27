# Python Cookbook

[![CI](https://github.com/johnburbridge/python-cookbook/actions/workflows/ci.yaml/badge.svg)](https://github.com/johnburbridge/python-cookbook/actions/workflows/ci.yaml)
[![codecov](https://codecov.io/gh/johnburbridge/python-cookbook/branch/main/graph/badge.svg)](https://codecov.io/gh/johnburbridge/python-cookbook)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains a collection of Python projects that exemplify common operations and design patterns in Python. It serves as a quick reference guide with practical examples (recipes) of how to implement frequently used libraries and design patterns in Python 3.11+.

## Development Setup

### Requirements
- Python 3.11+
- pip (Python package installer)
- [Go Task](https://taskfile.dev/) (optional, for task automation)

### Getting Started
1. Clone the repository
2. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
3. Set up Git hooks (optional, but recommended):
   ```bash
   ./hooks/install-hooks.sh
   ```

### Task Automation
This project uses [Go Task](https://taskfile.dev/) to automate common development tasks:
- `task setup-root-venv`: Creates and sets up the root virtual environment
- `task setup-recipe-venv RECIPE=<name>`: Sets up a recipe-specific virtual environment
- `task format RECIPE=<name>`: Formats code using black
- `task lint RECIPE=<name>`: Runs flake8 linting
- `task test RECIPE=<name>`: Runs tests for a specific recipe
- `task validate-recipe RECIPE=<name>`: Runs format, lint, and test for a recipe
- `task validate-all`: Validates all recipes in the repository

### Code Quality
This project uses several tools to maintain code quality:
- **black**: Code formatting
- **flake8**: Code linting
- **pytest**: Testing framework
- **pytest-cov**: Test coverage reporting

#### Git Hooks
- **pre-commit**: Runs black and flake8 on staged Python files
- **pre-push**: Runs tests for modified recipes before pushing

### Continuous Integration
The project uses GitHub Actions for CI, which runs on every push to main and pull requests:
- Runs tests against Python 3.11 and 3.12
- Enforces code formatting with black
- Runs linting with flake8
- Requires 70% test coverage
- Reports coverage to Codecov with component-based tracking:
  - Each recipe is tracked as a separate component
  - Cross-cutting components for tests and core implementations
  - Coverage status displayed in PR comments

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
