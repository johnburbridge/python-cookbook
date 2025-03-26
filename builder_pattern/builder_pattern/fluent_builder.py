from copy import deepcopy
from typing import Dict, List, Any, Optional, Union

from builder_pattern.meal import Meal, MealItem


class FluentMealBuilder:
    """
    A fluent builder for creating meals using method chaining.
    This is an alternative implementation of the Builder pattern that uses
    a fluent interface (method chaining) instead of separate steps.
    """
    
    def __init__(self) -> None:
        """
        Initialize the builder with an empty meal.
        """
        self._meal = Meal(name="Custom Meal")
    
    def with_name(self, name: str) -> 'FluentMealBuilder':
        """
        Set the meal name.
        
        Args:
            name: The name of the meal
            
        Returns:
            FluentMealBuilder: The builder instance for method chaining
        """
        self._meal.name = name
        return self
    
    def with_description(self, description: str) -> 'FluentMealBuilder':
        """
        Set the meal description.
        
        Args:
            description: The description of the meal
            
        Returns:
            FluentMealBuilder: The builder instance for method chaining
        """
        self._meal.description = description
        return self
    
    def with_price(self, price: float) -> 'FluentMealBuilder':
        """
        Set the meal price.
        
        Args:
            price: The price of the meal
            
        Returns:
            FluentMealBuilder: The builder instance for method chaining
        """
        self._meal.price = price
        return self
    
    def with_main_dish(self, dish: MealItem) -> 'FluentMealBuilder':
        """
        Add a main dish to the meal.
        
        Args:
            dish: The main dish to add
            
        Returns:
            FluentMealBuilder: The builder instance for method chaining
        """
        self._meal.main_dish = dish
        
        # Add appropriate allergens based on the dish
        if dish in (MealItem.BURGER, MealItem.SANDWICH):
            self._append_allergen("Gluten")
            
        if dish == MealItem.FISH:
            self._append_allergen("Fish")
            
        if dish == MealItem.PASTA:
            self._append_allergen("Gluten")
            
        return self
    
    def with_side_dish(self, dish: MealItem) -> 'FluentMealBuilder':
        """
        Add a side dish to the meal.
        
        Args:
            dish: The side dish to add
            
        Returns:
            FluentMealBuilder: The builder instance for method chaining
        """
        self._meal.side_dish = dish
        return self
    
    def with_drink(self, drink: MealItem) -> 'FluentMealBuilder':
        """
        Add a drink to the meal.
        
        Args:
            drink: The drink to add
            
        Returns:
            FluentMealBuilder: The builder instance for method chaining
        """
        self._meal.drink = drink
        return self
    
    def with_dessert(self, dessert: MealItem) -> 'FluentMealBuilder':
        """
        Add a dessert to the meal.
        
        Args:
            dessert: The dessert to add
            
        Returns:
            FluentMealBuilder: The builder instance for method chaining
        """
        self._meal.dessert = dessert
        
        # Add appropriate allergens based on the dessert
        if dessert in (MealItem.ICE_CREAM, MealItem.CAKE):
            self._append_allergen("Dairy")
            
        if dessert == MealItem.CAKE:
            self._append_allergen("Gluten")
            
        return self
    
    def with_appetizer(self, appetizer: MealItem) -> 'FluentMealBuilder':
        """
        Add an appetizer to the meal.
        
        Args:
            appetizer: The appetizer to add
            
        Returns:
            FluentMealBuilder: The builder instance for method chaining
        """
        self._meal.appetizer = appetizer
        return self
    
    def with_extras(self, extras: List[MealItem]) -> 'FluentMealBuilder':
        """
        Add extras to the meal.
        
        Args:
            extras: The extras to add
            
        Returns:
            FluentMealBuilder: The builder instance for method chaining
        """
        self._meal.extras = extras
        return self
    
    def with_nutrition_info(self, info: Dict[str, Any]) -> 'FluentMealBuilder':
        """
        Add nutrition information to the meal.
        
        Args:
            info: The nutrition information
            
        Returns:
            FluentMealBuilder: The builder instance for method chaining
        """
        self._meal.nutrition_info = info
        return self
    
    def with_allergen(self, allergen: str) -> 'FluentMealBuilder':
        """
        Add an allergen to the meal.
        
        Args:
            allergen: The allergen to add
            
        Returns:
            FluentMealBuilder: The builder instance for method chaining
        """
        self._append_allergen(allergen)
        return self
    
    def vegetarian(self) -> 'FluentMealBuilder':
        """
        Mark the meal as vegetarian.
        
        Returns:
            FluentMealBuilder: The builder instance for method chaining
        """
        self._meal.is_vegetarian = True
        return self
    
    def kids_meal(self) -> 'FluentMealBuilder':
        """
        Mark the meal as a kids meal.
        
        Returns:
            FluentMealBuilder: The builder instance for method chaining
        """
        self._meal.is_kids_meal = True
        return self
    
    def _append_allergen(self, allergen: str) -> None:
        """
        Helper method to append an allergen to the meal if it's not already included.
        
        Args:
            allergen: The allergen to append
        """
        if allergen not in self._meal.contains_allergens:
            self._meal.contains_allergens.append(allergen)
    
    def build(self) -> Meal:
        """
        Build and return the final meal.
        
        Returns:
            Meal: The constructed meal
        """
        # Return a deep copy to ensure builder is decoupled from the product
        return deepcopy(self._meal) 