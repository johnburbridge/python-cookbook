# Objectives

The purpose of this repository is to provide a collection of python projects which exemplify common operations and
design patterns in Python. It is intended to be used as a quick reference guide with practical examples (recipes) of
how to implement often used libraries and design patterns in Python 3.11+.

## Structure

Each subdirectory in the `python-cookbook` should follow a common structure as follows:
```
.
├── README.md
├── objectives.md
└── <example name>
    ├── README.md
    ├── <package_name>
    ├── requirements.txt
    ├── tests  
    └── venv
```
Where:
- README.md contains notes about the recipe, including references to further reading on the topic
- <example_name> is the name of the recipe
- <package_name> is the name of the package, most often the same as the recipe
- requirements.txt contains pip dependencies (from `pip freeze > requirements.txt`)
- tests contains unittests which show how to provide test coverage for the recipe
- venv contains the environment for this recipe (from `python3 -m venv venv`), though this should not be committed to git
- docker-compose.yml (optional) supports setting up infrastructure (web servers, databases, etc) which may be required for the recipe

## Recipes

1. The Strategy Pattern
2. The Factory Pattern
3. The Builder Pattern
4. The Observable Pattern
5. Generics in Python
6. Reading and writing JSON
7. Reading and writing YAML
8. Handling HTTP Requests
9. Data classes
10. Reading and writing from/to Postgres
11. Reading and writing from/to MongoDB
12. Reading and writing from/to Redis
