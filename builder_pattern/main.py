#!/usr/bin/env python3
"""
This script demonstrates the Builder Pattern with different meal builders.
It shows both the classic Builder Pattern with a Director and a Fluent
Builder implementation.
"""
from builder_pattern.meal import MealItem
from builder_pattern.concrete_builders import (
    RegularMealBuilder,
    VegetarianMealBuilder,
    ChildrenMealBuilder,
)
from builder_pattern.meal_director import MealDirector, MealConfig
from builder_pattern.fluent_builder import FluentMealBuilder
from builder_pattern.meal_builder import MealBuilder


def demonstrate_classic_builder():
    """
    Demonstrate the classic Builder Pattern with Director.
    """
    print("\n=== CLASSIC BUILDER PATTERN DEMONSTRATION ===\n")

    # Create builders
    regular_builder = RegularMealBuilder()
    vegetarian_builder = VegetarianMealBuilder()
    children_builder = ChildrenMealBuilder()

    # Create director
    director = MealDirector()

    # Build a regular basic meal
    director.set_builder(regular_builder)
    basic_meal = director.construct_basic_meal(name="Basic Burger Meal", price=8.99)
    print(basic_meal.display())
    print()

    # Build a regular standard meal
    standard_meal = director.construct_standard_meal(
        name="Standard Burger Meal", price=12.99
    )
    print(standard_meal.display())
    print()

    # Build a premium vegetarian meal
    director.set_builder(vegetarian_builder)
    premium_vegetarian = director.construct_premium_meal(
        name="Premium Vegetarian Meal",
        price=15.99,
        description="A complete vegetarian dining experience with all the extras.",
    )
    print(premium_vegetarian.display())
    print()

    # Build a children's meal with custom configuration using the MealConfig
    director.set_builder(children_builder)
    kids_meal_config = MealConfig(
        name="Fun Kids Meal",
        description="A special meal for the little ones with a fun surprise toy!",
        price=7.99,
        main_dish=True,
        side_dish=True,
        drink=True,
        dessert=True,
        extras=True,
    )
    custom_kids_meal = director.construct_custom_meal(kids_meal_config)
    print(custom_kids_meal.display())
    print()


def demonstrate_fluent_builder():
    """
    Demonstrate the Fluent Builder Pattern.
    """
    print("\n=== FLUENT BUILDER PATTERN DEMONSTRATION ===\n")

    # Create a custom meal using the fluent builder
    custom_meal = (
        FluentMealBuilder()
        .with_name("Custom Deluxe Meal")
        .with_description("Build your own perfect meal")
        .with_price(14.99)
        .with_main_dish(MealItem.CHICKEN)
        .with_side_dish(MealItem.RICE)
        .with_drink(MealItem.WATER)
        .with_dessert(MealItem.CAKE)
        .build()
    )
    print(custom_meal.display())
    print()

    # Create a vegetarian meal using the fluent builder
    vegetarian_meal = (
        FluentMealBuilder()
        .with_name("Custom Vegetarian Delight")
        .with_price(13.99)
        .with_main_dish(MealItem.PASTA)
        .with_side_dish(MealItem.SALAD)
        .with_drink(MealItem.JUICE)
        .with_dessert(MealItem.FRUIT)
        .with_nutrition_info(
            {"calories": 750, "protein": 22, "carbs": 110, "fat": 20, "fiber": 12}
        )
        .vegetarian()
        .build()
    )
    print(vegetarian_meal.display())
    print()

    # Create a kids meal using the fluent builder
    kids_meal = (
        FluentMealBuilder()
        .with_name("Build Your Own Kids Meal")
        .with_price(8.99)
        .with_main_dish(MealItem.SANDWICH)
        .with_side_dish(MealItem.FRIES)
        .with_drink(MealItem.JUICE)
        .with_extras([MealItem.TOY])
        .kids_meal()
        .build()
    )
    print(kids_meal.display())
    print()


def main() -> None:
    """Run the meal builder demo."""
    print("=== Meal Builder Demo ===\n")

    # Create a builder
    builder = MealBuilder()

    # Build a breakfast meal
    breakfast = (
        builder.reset()
        .add_main("Eggs Benedict")
        .add_side("Hash Browns")
        .add_drink("Orange Juice")
        .add_dessert("Fresh Fruit")
        .build()
    )

    print("Breakfast:")
    print(breakfast)

    # Build a lunch meal
    lunch = (
        builder.reset()
        .add_main("Grilled Chicken Sandwich")
        .add_side("French Fries")
        .add_drink("Iced Tea")
        .build()
    )

    print("\nLunch:")
    print(lunch)

    # Build a dinner meal
    dinner = (
        builder.reset()
        .add_main("Steak")
        .add_side("Mashed Potatoes")
        .add_side("Steamed Vegetables")
        .add_drink("Red Wine")
        .add_dessert("Chocolate Cake")
        .build()
    )

    print("\nDinner:")
    print(dinner)


if __name__ == "__main__":
    main()
