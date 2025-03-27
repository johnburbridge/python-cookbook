"""Module containing the Meal and MealItem classes."""

from enum import Enum, auto
from typing import List, Optional, Dict, Any
from dataclasses import dataclass, field


class MealItem(Enum):
    """Enumeration of meal components."""
    BURGER = auto()
    CHICKEN = auto()
    FISH = auto()
    PASTA = auto()
    SANDWICH = auto()
    FRIES = auto()
    SALAD = auto()
    RICE = auto()
    SOFT_DRINK = auto()
    JUICE = auto()
    WATER = auto()
    ICE_CREAM = auto()
    CAKE = auto()
    FRUIT = auto()
    SOUP = auto()
    TOY = auto()


@dataclass
class Meal:
    """Class representing a meal with various components."""
    name: str
    description: Optional[str] = None
    price: Optional[float] = None
    main_dish: Optional[MealItem] = None
    side_dish: Optional[MealItem] = None
    drink: Optional[MealItem] = None
    dessert: Optional[MealItem] = None
    appetizer: Optional[MealItem] = None
    extras: List[MealItem] = field(default_factory=list)
    contains_allergens: List[str] = field(default_factory=list)
    nutrition_info: Dict[str, Any] = field(default_factory=dict)
    is_vegetarian: bool = False
    is_kids_meal: bool = False
    
    def display(self) -> str:
        """Display the meal information in a formatted string."""
        lines = []
        
        if self.name:
            lines.append(f"=== {self.name} ===")
        
        if self.description:
            lines.append(f"{self.description}")
        
        if self.price is not None:
            lines.append(f"Price: ${self.price:.2f}")
        
        if self.main_dish:
            lines.append(f"Main: {self.main_dish.name.title().replace('_', ' ')}")
        
        if self.side_dish:
            lines.append(f"Side: {self.side_dish.name.title().replace('_', ' ')}")
        
        if self.appetizer:
            lines.append(f"Appetizer: {self.appetizer.name.title().replace('_', ' ')}")
        
        if self.drink:
            lines.append(f"Drink: {self.drink.name.title().replace('_', ' ')}")
        
        if self.dessert:
            lines.append(f"Dessert: {self.dessert.name.title().replace('_', ' ')}")
        
        if self.extras:
            extras_list = ", ".join([item.name.title().replace('_', ' ') for item in self.extras])
            lines.append(f"Extras: {extras_list}")
        
        if self.nutrition_info:
            nutrition_str = ", ".join([f"{k}: {v}" for k, v in self.nutrition_info.items()])
            lines.append(f"Nutrition: {nutrition_str}")
        
        if self.is_vegetarian:
            lines.append("Vegetarian: Yes")
        
        if self.is_kids_meal:
            lines.append("Kids Meal: Yes")
        
        if self.contains_allergens:
            allergens = ", ".join(self.contains_allergens)
            lines.append(f"Allergens: {allergens}")
        
        return "\n".join(lines)
    
    def total_items(self) -> int:
        """Count the total number of items in the meal."""
        count = 0
        if self.main_dish:
            count += 1
        if self.side_dish:
            count += 1
        if self.appetizer:
            count += 1
        if self.drink:
            count += 1
        if self.dessert:
            count += 1
        count += len(self.extras)
        return count 