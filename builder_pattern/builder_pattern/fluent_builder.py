from typing import Dict, Any, List, Self
from copy import deepcopy

from builder_pattern.meal import Meal, MealItem


class FluentMealBuilder:
    """
    A fluent builder implementation for creating meals.
    This builder uses method chaining (returning self from each method).
    """
    
    def __init__(self):
        """
        Initialize the builder with a new meal.
        """
        self._meal = Meal(name="Custom Meal")
    
    def with_name(self, name: str) -> Self:
        """
        Set the name of the meal.
        
        Args:
            name: The name of the meal
            
        Returns:
            Self: The builder instance for method chaining
        """
        self._meal.name = name
        return self
    
    def with_description(self, description: str) -> Self:
        """
        Set the description of the meal.
        
        Args:
            description: The description of the meal
            
        Returns:
            Self: The builder instance for method chaining
        """
        self._meal.description = description
        return self
    
    def with_price(self, price: float) -> Self:
        """
        Set the price of the meal.
        
        Args:
            price: The price of the meal
            
        Returns:
            Self: The builder instance for method chaining
        """
        self._meal.price = price
        return self
    
    def with_main_dish(self, main_dish: MealItem) -> Self:
        """
        Add a main dish to the meal.
        
        Args:
            main_dish: The main dish item
            
        Returns:
            Self: The builder instance for method chaining
        """
        self._meal.main_dish = main_dish
        
        # Add allergens based on the main dish
        if main_dish in [MealItem.BURGER, MealItem.SANDWICH, MealItem.PASTA]:
            if "Gluten" not in self._meal.contains_allergens:
                self._meal.contains_allergens.append("Gluten")
        
        if main_dish == MealItem.BURGER:
            if "Dairy" not in self._meal.contains_allergens:
                self._meal.contains_allergens.append("Dairy")
        
        return self
    
    def with_side_dish(self, side_dish: MealItem) -> Self:
        """
        Add a side dish to the meal.
        
        Args:
            side_dish: The side dish item
            
        Returns:
            Self: The builder instance for method chaining
        """
        self._meal.side_dish = side_dish
        return self
    
    def with_drink(self, drink: MealItem) -> Self:
        """
        Add a drink to the meal.
        
        Args:
            drink: The drink item
            
        Returns:
            Self: The builder instance for method chaining
        """
        self._meal.drink = drink
        return self
    
    def with_dessert(self, dessert: MealItem) -> Self:
        """
        Add a dessert to the meal.
        
        Args:
            dessert: The dessert item
            
        Returns:
            Self: The builder instance for method chaining
        """
        self._meal.dessert = dessert
        
        # Add allergens based on the dessert
        if dessert in [MealItem.ICE_CREAM, MealItem.CAKE]:
            if "Dairy" not in self._meal.contains_allergens:
                self._meal.contains_allergens.append("Dairy")
        
        return self
    
    def with_appetizer(self, appetizer: MealItem) -> Self:
        """
        Add an appetizer to the meal.
        
        Args:
            appetizer: The appetizer item
            
        Returns:
            Self: The builder instance for method chaining
        """
        self._meal.appetizer = appetizer
        return self
    
    def with_extras(self, extras: List[MealItem]) -> Self:
        """
        Add extras to the meal.
        
        Args:
            extras: The list of extra items
            
        Returns:
            Self: The builder instance for method chaining
        """
        self._meal.extras = extras
        return self
    
    def with_nutrition_info(self, nutrition_info: Dict[str, Any]) -> Self:
        """
        Add nutrition information to the meal.
        
        Args:
            nutrition_info: Dictionary with nutrition information
            
        Returns:
            Self: The builder instance for method chaining
        """
        self._meal.nutrition_info = nutrition_info
        return self
    
    def vegetarian(self) -> Self:
        """
        Mark the meal as vegetarian.
        
        Returns:
            Self: The builder instance for method chaining
        """
        self._meal.is_vegetarian = True
        return self
    
    def kids_meal(self) -> Self:
        """
        Mark the meal as a kids meal.
        
        Returns:
            Self: The builder instance for method chaining
        """
        self._meal.is_kids_meal = True
        return self
    
    def with_allergen(self, allergen: str) -> Self:
        """
        Add an allergen to the meal.
        
        Args:
            allergen: The allergen to add
            
        Returns:
            Self: The builder instance for method chaining
        """
        if allergen not in self._meal.contains_allergens:
            self._meal.contains_allergens.append(allergen)
        return self
    
    def build(self) -> Meal:
        """
        Build and return the meal.
        
        Returns:
            Meal: The constructed meal
        """
        return deepcopy(self._meal) 