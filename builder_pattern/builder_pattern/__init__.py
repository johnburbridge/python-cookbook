"""
Builder Pattern Implementation

This module provides a complete implementation of the Builder Pattern
for meal preparation.
"""

from .meal import Meal, MealItem
from .meal_builder import MealBuilder
from .concrete_builders import (
    RegularMealBuilder,
    VegetarianMealBuilder,
    ChildrenMealBuilder,
)
from .meal_director import MealDirector, MealConfig
from .fluent_builder import FluentMealBuilder

__all__ = [
    "Meal",
    "MealItem",
    "MealBuilder",
    "RegularMealBuilder",
    "VegetarianMealBuilder",
    "ChildrenMealBuilder",
    "MealDirector",
    "MealConfig",
    "FluentMealBuilder",
]
