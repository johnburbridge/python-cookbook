# Builder Pattern Implementation

This module demonstrates the Builder Pattern for meal preparation. The Builder Pattern is a creational design pattern used to construct complex objects step by step, allowing for the creation of different representations of an object using the same construction process.

## Components

1. **Meal** (`meal.py`): The product class representing the complex object being built.
2. **MealItem** (`meal.py`): An enumeration of available meal components.
3. **MealBuilder** (`meal_builder.py`): The abstract builder interface defining methods for building meal parts.
4. **Concrete Builders** (`concrete_builders.py`):
   - `RegularMealBuilder`: Builds standard meals with regular options.
   - `VegetarianMealBuilder`: Builds vegetarian meals with plant-based options.
   - `ChildrenMealBuilder`: Builds kid-friendly meals with appropriate portions and toys.
5. **MealDirector** (`meal_director.py`): Directs the building process, coordinating the construction of meals using a builder.
6. **MealConfig** (`meal_director.py`): A strongly-typed configuration class for customizing meal construction.
7. **FluentMealBuilder** (`fluent_builder.py`): An alternative implementation using the fluent interface pattern.

## Usage Examples

### Classic Builder Pattern with Director

```python
# Create a builder
builder = RegularMealBuilder()

# Create a director and set the builder
director = MealDirector()
director.set_builder(builder)

# Construct different types of meals
basic_meal = director.construct_basic_meal(name="Basic Burger Meal", price=8.99)
standard_meal = director.construct_standard_meal()
premium_meal = director.construct_premium_meal(
    name="Premium Burger Feast",
    price=15.99,
    description="Our signature premium meal with all the fixings"
)

# Custom configuration using MealConfig
meal_config = MealConfig(
    name="Custom Burger Meal",
    price=12.99,
    main_dish=True,
    side_dish=True,
    drink=True,
    dessert=False,
    nutrition_info=True
)
custom_meal = director.construct_custom_meal(meal_config)
```

### Fluent Builder (Method Chaining)

```python
# Create a meal using the fluent interface
meal = (
    FluentMealBuilder()
    .with_name("Custom Fish Meal")
    .with_description("A delicious fish meal with rice")
    .with_price(14.99)
    .with_main_dish(MealItem.FISH)
    .with_side_dish(MealItem.RICE)
    .with_drink(MealItem.WATER)
    .with_dessert(MealItem.CAKE)
    .with_nutrition_info({
        "calories": 750,
        "protein": 35,
        "carbs": 65,
        "fat": 20
    })
    .build()
)

# Display the meal
print(meal.display())
```

## Benefits of the Builder Pattern

1. **Separation of Concerns**: The construction process is separate from the object representation.
2. **Step-by-step Construction**: Complex objects can be created step by step.
3. **Different Representations**: The same construction process can create different representations.
4. **Encapsulation**: The internal structure of the product is hidden from the client.
5. **Fluent Interface**: The fluent builder implementation allows for a more readable and chainable API.
6. **Type Safety**: The `MealConfig` class provides strongly-typed configuration options, reducing runtime errors.

## Testing

Run the tests using pytest:

```bash
python -m pytest tests/test_builders.py -v
```

## Running the Demo

```bash
python main.py
```

This will run demonstrations of both the classic Builder Pattern with a Director and the Fluent Builder pattern. 