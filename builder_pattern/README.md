# Builder Pattern Implementation - Meal Preparation System

This project demonstrates the Builder Pattern in Python through a meal preparation system. The Builder Pattern is a creational design pattern that allows for the construction of complex objects step by step, separating the construction process from the actual representation.

## Overview

The Builder Pattern is particularly useful when:
- An object needs to be created with many optional parameters
- The construction process should be independent of the parts that make up the object
- Different representations of the object can be created using the same construction process

## Implementation Details

This implementation showcases two variations of the Builder Pattern:

### 1. Classic Builder Pattern with Director

- `MealBuilder` (Abstract Builder): Defines the interface for creating parts of a meal
- Concrete Builders:
  - `RegularMealBuilder`: Creates regular meals with standard options
  - `VegetarianMealBuilder`: Creates vegetarian meals with appropriate substitutes
  - `ChildrenMealBuilder`: Creates kid-friendly meals with special features
- `MealDirector`: Controls the building process and ensures meals are built in the correct order
- `Meal` (Product): The complex object being built

### 2. Fluent Builder Pattern

- `FluentMealBuilder`: Provides a fluent interface for building meals using method chaining
- This approach offers a more concise, readable alternative for constructing meals

## Key Features

- Support for different meal types (regular, vegetarian, children's meals)
- Allergen tracking based on meal components
- Nutrition information
- Customizable meal configurations
- Both classic and fluent builder implementations

## File Structure

- `meal.py`: Contains the `Meal` class and `MealItem` enum
- `meal_builder.py`: Contains the abstract `MealBuilder` class
- `concrete_builders.py`: Contains concrete builder implementations
- `meal_director.py`: Contains the `MealDirector` class and `MealConfig` dataclass
- `fluent_builder.py`: Contains the `FluentMealBuilder` implementation
- `main.py`: Demo script showing how to use both builder implementations
- `tests/`: Unit tests for the builder implementation

## Usage Example

```python
# Using the classic builder with director
director = MealDirector()
builder = RegularMealBuilder()
director.set_builder(builder)

basic_meal = director.construct_basic_meal()
standard_meal = director.construct_standard_meal()
premium_meal = director.construct_premium_meal()

# Using the fluent builder
custom_meal = (
    FluentMealBuilder()
    .with_name("Custom Meal")
    .with_price(12.99)
    .with_main_dish(MealItem.FISH)
    .with_side_dish(MealItem.RICE)
    .with_drink(MealItem.WATER)
    .with_dessert(MealItem.CAKE)
    .build()
)
```

## Running the Demo

To run the demonstration:

```
python -m builder_pattern.main
```

## Running Tests

To run the tests:

```
python -m unittest discover -s builder_pattern/tests
```

## Benefits of This Implementation

1. **Flexibility**: Easily create different meal configurations without complex constructors
2. **Separation of Concerns**: Building process is separate from the meal representation
3. **Step-by-Step Construction**: Control the exact sequence of meal creation
4. **Multiple Representations**: Create different types of meals using the same building process
5. **Fluent API**: Optional fluent interface for more readable code 