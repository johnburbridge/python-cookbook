"""Module containing the MealDirector and MealConfig classes."""

from dataclasses import dataclass
from typing import Dict, Any, Optional
from .meal_builder import MealBuilder
from .meal import Meal


@dataclass
class MealConfig:
    """Configuration for meal construction."""

    name: str
    price: float
    description: Optional[str] = None
    main_dish: bool = False
    side_dish: bool = False
    drink: bool = False
    dessert: bool = False
    appetizer: bool = False
    extras: bool = False
    nutrition_info: bool = False


class MealDirector:
    """Director class that constructs meals using a builder."""

    def __init__(self):
        """Initialize the director without a builder."""
        self._builder: Optional[MealBuilder] = None

    def set_builder(self, builder: MealBuilder) -> None:
        """Set the builder to use."""
        self._builder = builder

    def _check_builder(self) -> None:
        """Check if a builder is set."""
        if not self._builder:
            raise ValueError("No builder set. Call set_builder() first.")

    def construct_basic_meal(
        self, name: str = "Basic Meal", price: float = 8.99
    ) -> Meal:
        """Construct a basic meal with just main dish and drink."""
        self._check_builder()
        self._builder.reset()
        self._builder.set_name(name)
        self._builder.set_price(price)
        self._builder.add_main_dish()
        self._builder.add_drink()
        return self._builder.get_meal()

    def construct_standard_meal(self) -> Meal:
        """Construct a standard meal with main dish, side dish, and drink."""
        self._check_builder()
        self._builder.reset()
        self._builder.set_name("Standard Meal")
        self._builder.set_price(12.99)
        self._builder.add_main_dish()
        self._builder.add_side_dish()
        self._builder.add_drink()
        return self._builder.get_meal()

    def construct_premium_meal(
        self,
        name: str = "Premium Meal",
        price: float = 15.99,
        description: str = "A complete premium meal",
    ) -> Meal:
        """Construct a premium meal with all components."""
        self._check_builder()
        self._builder.reset()
        self._builder.set_name(name)
        self._builder.set_price(price)
        self._builder.set_description(description)
        self._builder.add_appetizer()
        self._builder.add_main_dish()
        self._builder.add_side_dish()
        self._builder.add_drink()
        self._builder.add_dessert()
        self._builder.add_extras()
        self._builder.add_nutrition_info()
        return self._builder.get_meal()

    def construct_custom_meal(self, config: MealConfig) -> Meal:
        """Construct a custom meal based on configuration."""
        self._check_builder()
        self._builder.reset()
        self._builder.set_name(config.name)
        self._builder.set_price(config.price)

        if config.description:
            self._builder.set_description(config.description)
        if config.main_dish:
            self._builder.add_main_dish()
        if config.side_dish:
            self._builder.add_side_dish()
        if config.drink:
            self._builder.add_drink()
        if config.dessert:
            self._builder.add_dessert()
        if config.appetizer:
            self._builder.add_appetizer()
        if config.extras:
            self._builder.add_extras()
        if config.nutrition_info:
            self._builder.add_nutrition_info()

        return self._builder.get_meal()

    def construct_meal_from_dict(self, config: Dict[str, Any]) -> Meal:
        """Construct a meal from a dictionary configuration."""
        meal_config = MealConfig(
            name=config.get("name", "Custom Meal"),
            price=config.get("price", 10.99),
            description=config.get("description"),
            main_dish=config.get("main_dish", False),
            side_dish=config.get("side_dish", False),
            drink=config.get("drink", False),
            dessert=config.get("dessert", False),
            appetizer=config.get("appetizer", False),
            extras=config.get("extras", False),
            nutrition_info=config.get("nutrition_info", False),
        )
        return self.construct_custom_meal(meal_config)
