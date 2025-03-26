from typing import Dict, Any, List
from copy import deepcopy

from builder_pattern.meal import Meal, MealItem
from builder_pattern.meal_builder import MealBuilder


class RegularMealBuilder(MealBuilder):
    """
    Concrete builder for regular (standard) meals.
    """
    
    def __init__(self):
        """
        Initialize the builder.
        """
        self.reset()
    
    def reset(self) -> None:
        """
        Reset the builder to create a new meal.
        """
        self._meal = Meal(name="Regular Meal")
    
    def set_name(self, name: str) -> None:
        """
        Set the name of the meal.
        
        Args:
            name: The name of the meal
        """
        self._meal.name = name
    
    def set_description(self, description: str) -> None:
        """
        Set the description of the meal.
        
        Args:
            description: The description of the meal
        """
        self._meal.description = description
    
    def set_price(self, price: float) -> None:
        """
        Set the price of the meal.
        
        Args:
            price: The price of the meal
        """
        self._meal.price = price
    
    def add_main_dish(self) -> None:
        """
        Add a main dish to the meal.
        For a regular meal, we'll use a burger.
        """
        self._meal.main_dish = MealItem.BURGER
        self._meal.contains_allergens.append("Gluten")
        self._meal.contains_allergens.append("Dairy")
    
    def add_side_dish(self) -> None:
        """
        Add a side dish to the meal.
        For a regular meal, we'll use fries.
        """
        self._meal.side_dish = MealItem.FRIES
    
    def add_drink(self) -> None:
        """
        Add a drink to the meal.
        For a regular meal, we'll use a soft drink.
        """
        self._meal.drink = MealItem.SOFT_DRINK
    
    def add_dessert(self) -> None:
        """
        Add a dessert to the meal.
        For a regular meal, we'll use ice cream.
        """
        self._meal.dessert = MealItem.ICE_CREAM
        if "Dairy" not in self._meal.contains_allergens:
            self._meal.contains_allergens.append("Dairy")
    
    def add_appetizer(self) -> None:
        """
        Add an appetizer to the meal.
        For a regular meal, we'll use a salad.
        """
        self._meal.appetizer = MealItem.SALAD
    
    def add_extras(self) -> None:
        """
        Add extras to the meal.
        For a regular meal, no extras.
        """
        pass
    
    def add_nutrition_info(self) -> None:
        """
        Add nutrition information to the meal.
        """
        self._meal.nutrition_info = {
            "calories": 1200,
            "protein": 35,
            "carbs": 140,
            "fat": 60
        }
    
    def get_meal(self) -> Meal:
        """
        Return the constructed meal.
        
        Returns:
            Meal: The constructed meal
        """
        return deepcopy(self._meal)


class VegetarianMealBuilder(MealBuilder):
    """
    Concrete builder for vegetarian meals.
    """
    
    def __init__(self):
        """
        Initialize the builder.
        """
        self.reset()
    
    def reset(self) -> None:
        """
        Reset the builder to create a new meal.
        """
        self._meal = Meal(name="Vegetarian Meal")
        self._meal.is_vegetarian = True
    
    def set_name(self, name: str) -> None:
        """
        Set the name of the meal.
        
        Args:
            name: The name of the meal
        """
        self._meal.name = name
    
    def set_description(self, description: str) -> None:
        """
        Set the description of the meal.
        
        Args:
            description: The description of the meal
        """
        self._meal.description = description
    
    def set_price(self, price: float) -> None:
        """
        Set the price of the meal.
        
        Args:
            price: The price of the meal
        """
        self._meal.price = price
    
    def add_main_dish(self) -> None:
        """
        Add a main dish to the meal.
        For a vegetarian meal, we'll use pasta.
        """
        self._meal.main_dish = MealItem.PASTA
        self._meal.contains_allergens.append("Gluten")
    
    def add_side_dish(self) -> None:
        """
        Add a side dish to the meal.
        For a vegetarian meal, we'll use a salad.
        """
        self._meal.side_dish = MealItem.SALAD
    
    def add_drink(self) -> None:
        """
        Add a drink to the meal.
        For a vegetarian meal, we'll use juice.
        """
        self._meal.drink = MealItem.JUICE
    
    def add_dessert(self) -> None:
        """
        Add a dessert to the meal.
        For a vegetarian meal, we'll use fruit.
        """
        self._meal.dessert = MealItem.FRUIT
    
    def add_appetizer(self) -> None:
        """
        Add an appetizer to the meal.
        For a vegetarian meal, we'll use soup.
        """
        self._meal.appetizer = MealItem.SOUP
    
    def add_extras(self) -> None:
        """
        Add extras to the meal.
        For a vegetarian meal, add extra vegetables.
        """
        self._meal.extras = [MealItem.SALAD]  # Extra veggies represented as a salad
    
    def add_nutrition_info(self) -> None:
        """
        Add nutrition information to the meal.
        """
        self._meal.nutrition_info = {
            "calories": 800,
            "protein": 20,
            "carbs": 120,
            "fat": 25,
            "fiber": 15
        }
    
    def get_meal(self) -> Meal:
        """
        Return the constructed meal.
        
        Returns:
            Meal: The constructed meal
        """
        return deepcopy(self._meal)


class ChildrenMealBuilder(MealBuilder):
    """
    Concrete builder for children's meals.
    """
    
    def __init__(self):
        """
        Initialize the builder.
        """
        self.reset()
    
    def reset(self) -> None:
        """
        Reset the builder to create a new meal.
        """
        self._meal = Meal(name="Children's Meal")
        self._meal.is_kids_meal = True
    
    def set_name(self, name: str) -> None:
        """
        Set the name of the meal.
        
        Args:
            name: The name of the meal
        """
        self._meal.name = name
    
    def set_description(self, description: str) -> None:
        """
        Set the description of the meal.
        
        Args:
            description: The description of the meal
        """
        self._meal.description = description
    
    def set_price(self, price: float) -> None:
        """
        Set the price of the meal.
        
        Args:
            price: The price of the meal
        """
        self._meal.price = price
    
    def add_main_dish(self) -> None:
        """
        Add a main dish to the meal.
        For a children's meal, we'll use chicken.
        """
        self._meal.main_dish = MealItem.CHICKEN
    
    def add_side_dish(self) -> None:
        """
        Add a side dish to the meal.
        For a children's meal, we'll use fries.
        """
        self._meal.side_dish = MealItem.FRIES
    
    def add_drink(self) -> None:
        """
        Add a drink to the meal.
        For a children's meal, we'll use juice.
        """
        self._meal.drink = MealItem.JUICE
    
    def add_dessert(self) -> None:
        """
        Add a dessert to the meal.
        For a children's meal, we'll use ice cream.
        """
        self._meal.dessert = MealItem.ICE_CREAM
        self._meal.contains_allergens.append("Dairy")
    
    def add_appetizer(self) -> None:
        """
        Add an appetizer to the meal.
        Children's meals usually don't have appetizers.
        """
        pass
    
    def add_extras(self) -> None:
        """
        Add extras to the meal.
        For a children's meal, add a toy.
        """
        self._meal.extras = [MealItem.TOY]
    
    def add_nutrition_info(self) -> None:
        """
        Add nutrition information to the meal.
        """
        self._meal.nutrition_info = {
            "calories": 650,
            "protein": 25,
            "carbs": 80,
            "fat": 30
        }
    
    def get_meal(self) -> Meal:
        """
        Return the constructed meal.
        
        Returns:
            Meal: The constructed meal
        """
        return deepcopy(self._meal) 