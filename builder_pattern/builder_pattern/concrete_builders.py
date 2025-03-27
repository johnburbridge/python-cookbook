"""Module containing concrete implementations of MealBuilder."""

from .meal_builder import MealBuilder
from .meal import MealItem


class RegularMealBuilder(MealBuilder):
    """Builder for regular meals."""

    def add_main_dish(self) -> None:
        """Add a burger as the main dish."""
        self._meal.main_dish = MealItem.BURGER
        self._meal.contains_allergens.append("Gluten")

    def add_side_dish(self) -> None:
        """Add fries as the side dish."""
        self._meal.side_dish = MealItem.FRIES

    def add_drink(self) -> None:
        """Add a soft drink."""
        self._meal.drink = MealItem.SOFT_DRINK

    def add_dessert(self) -> None:
        """Add ice cream as dessert."""
        self._meal.dessert = MealItem.ICE_CREAM
        self._meal.contains_allergens.append("Dairy")

    def add_nutrition_info(self) -> None:
        """Add nutrition information."""
        self._meal.nutrition_info.update({
            "calories": 1200,
            "protein": "30g",
            "carbs": "150g",
            "fat": "45g"
        })


class VegetarianMealBuilder(MealBuilder):
    """Builder for vegetarian meals."""

    def __init__(self):
        """Initialize with vegetarian flag set."""
        super().__init__()
        self._meal.is_vegetarian = True

    def add_main_dish(self) -> None:
        """Add pasta as the main dish."""
        self._meal.main_dish = MealItem.PASTA
        self._meal.contains_allergens.append("Gluten")

    def add_side_dish(self) -> None:
        """Add salad as the side dish."""
        self._meal.side_dish = MealItem.SALAD

    def add_drink(self) -> None:
        """Add juice as the drink."""
        self._meal.drink = MealItem.JUICE

    def add_dessert(self) -> None:
        """Add fruit as dessert."""
        self._meal.dessert = MealItem.FRUIT

    def add_extras(self) -> None:
        """Add extra veggies."""
        self._meal.extras.append(MealItem.SALAD)


class ChildrenMealBuilder(MealBuilder):
    """Builder for children's meals."""

    def __init__(self):
        """Initialize with kids meal flag set."""
        super().__init__()
        self._meal.is_kids_meal = True

    def add_main_dish(self) -> None:
        """Add chicken as the main dish."""
        self._meal.main_dish = MealItem.CHICKEN

    def add_side_dish(self) -> None:
        """Add fries as the side dish."""
        self._meal.side_dish = MealItem.FRIES

    def add_drink(self) -> None:
        """Add juice as the drink."""
        self._meal.drink = MealItem.JUICE

    def add_dessert(self) -> None:
        """Add ice cream as dessert."""
        self._meal.dessert = MealItem.ICE_CREAM
        self._meal.contains_allergens.append("Dairy")

    def add_extras(self) -> None:
        """Add a toy."""
        self._meal.extras.append(MealItem.TOY)
