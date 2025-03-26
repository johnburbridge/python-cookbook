from enum import Enum, auto
from typing import List, Optional, Dict, Any
from dataclasses import dataclass, field


class MealItem(Enum):
    """
    Enum representing different types of meal items.
    """
    BURGER = auto()
    SANDWICH = auto()
    CHICKEN = auto()
    FISH = auto()
    RICE = auto()
    PASTA = auto()
    FRIES = auto()
    SALAD = auto()
    SOUP = auto()
    SOFT_DRINK = auto()
    JUICE = auto()
    WATER = auto()
    ICE_CREAM = auto()
    CAKE = auto()
    FRUIT = auto()
    TOY = auto()


@dataclass
class Meal:
    """
    The product class - represents a meal with various components.
    """
    name: str
    description: str = ""
    price: float = 0.0
    main_dish: Optional[MealItem] = None
    side_dish: Optional[MealItem] = None
    drink: Optional[MealItem] = None
    dessert: Optional[MealItem] = None
    appetizer: Optional[MealItem] = None
    extras: List[MealItem] = field(default_factory=list)
    nutrition_info: Dict[str, Any] = field(default_factory=dict)
    is_vegetarian: bool = False
    is_kids_meal: bool = False
    contains_allergens: List[str] = field(default_factory=list)
    
    def total_items(self) -> int:
        """
        Calculate the total number of items in the meal.
        
        Returns:
            int: Total number of items
        """
        count = 0
        if self.main_dish:
            count += 1
        if self.side_dish:
            count += 1
        if self.drink:
            count += 1
        if self.dessert:
            count += 1
        if self.appetizer:
            count += 1
        count += len(self.extras)
        return count
    
    def display(self) -> str:
        """
        Return a string representation of the meal.
        
        Returns:
            str: Description of the meal
        """
        meal_info = [f"=== {self.name} ==="]
        
        if self.description:
            meal_info.append(f"{self.description}")
        
        meal_info.append(f"Price: ${self.price:.2f}")
        
        if self.main_dish:
            meal_info.append(f"Main: {self.main_dish.name.replace('_', ' ').title()}")
        
        if self.side_dish:
            meal_info.append(f"Side: {self.side_dish.name.replace('_', ' ').title()}")
        
        if self.appetizer:
            meal_info.append(f"Appetizer: {self.appetizer.name.replace('_', ' ').title()}")
        
        if self.drink:
            meal_info.append(f"Drink: {self.drink.name.replace('_', ' ').title()}")
        
        if self.dessert:
            meal_info.append(f"Dessert: {self.dessert.name.replace('_', ' ').title()}")
        
        if self.extras:
            extras_str = ", ".join([extra.name.replace('_', ' ').title() for extra in self.extras])
            meal_info.append(f"Extras: {extras_str}")
        
        if self.nutrition_info:
            nutrition_str = ", ".join([f"{key}: {value}" for key, value in self.nutrition_info.items()])
            meal_info.append(f"Nutrition: {nutrition_str}")
        
        if self.is_vegetarian:
            meal_info.append("Vegetarian: Yes")
        
        if self.is_kids_meal:
            meal_info.append("Kids Meal: Yes")
        
        if self.contains_allergens:
            allergens_str = ", ".join(self.contains_allergens)
            meal_info.append(f"Allergens: {allergens_str}")
        
        return "\n".join(meal_info) 