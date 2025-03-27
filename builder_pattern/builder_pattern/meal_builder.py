"""Module containing the abstract MealBuilder class."""

from abc import ABC, abstractmethod
from .meal import Meal


class MealBuilder(ABC):
    """Abstract base class for meal builders."""

    def __init__(self):
        """Initialize the builder with a reset."""
        self.reset()

    def reset(self) -> None:
        """Reset the builder to create a new meal."""
        self._meal = Meal(name="")

    @property
    def meal(self) -> Meal:
        """Get the built meal."""
        return self._meal

    def get_meal(self) -> Meal:
        """Get the built meal and reset the builder."""
        meal = self.meal
        self.reset()
        return meal

    def set_name(self, name: str) -> None:
        """Set the meal name."""
        self._meal.name = name

    def set_description(self, description: str) -> None:
        """Set the meal description."""
        self._meal.description = description

    def set_price(self, price: float) -> None:
        """Set the meal price."""
        self._meal.price = price

    @abstractmethod
    def add_main_dish(self) -> None:
        """Add the main dish to the meal."""
        pass

    @abstractmethod
    def add_side_dish(self) -> None:
        """Add the side dish to the meal."""
        pass

    @abstractmethod
    def add_drink(self) -> None:
        """Add the drink to the meal."""
        pass

    @abstractmethod
    def add_dessert(self) -> None:
        """Add the dessert to the meal."""
        pass

    def add_appetizer(self) -> None:
        """Add an appetizer to the meal."""
        pass

    def add_extras(self) -> None:
        """Add extras to the meal."""
        pass

    def add_nutrition_info(self) -> None:
        """Add nutrition information to the meal."""
        pass
