from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List

from builder_pattern.meal_builder import MealBuilder
from builder_pattern.meal import Meal, MealItem


@dataclass
class MealConfig:
    """
    Configuration class for customizing meal construction.
    Provides a strongly-typed, self-documenting way to specify meal options.
    """
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    main_dish: bool = False
    side_dish: bool = False
    drink: bool = False
    dessert: bool = False
    appetizer: bool = False
    extras: bool = False
    nutrition_info: bool = False
    nutrition_values: Optional[Dict[str, Any]] = None


class MealDirector:
    """
    Director class that controls the building process.
    It works with the builder interface to build complex objects.
    """
    
    def __init__(self, builder: MealBuilder = None):
        """
        Initialize the director with an optional builder.
        
        Args:
            builder: The builder to use
        """
        self._builder = builder
    
    def set_builder(self, builder: MealBuilder) -> None:
        """
        Set the builder instance.
        
        Args:
            builder: The builder to use
        """
        self._builder = builder
    
    def construct_basic_meal(self, name: str = None, price: float = None) -> Meal:
        """
        Construct a basic meal with only main dish and drink.
        
        Args:
            name: Optional name for the meal
            price: Optional price for the meal
            
        Returns:
            Meal: The constructed meal
            
        Raises:
            ValueError: If no builder is set
        """
        if not self._builder:
            raise ValueError("No builder set. Use set_builder() to set a builder.")
        
        self._builder.reset()
        
        if name:
            self._builder.set_name(name)
        
        if price:
            self._builder.set_price(price)
            
        self._builder.add_main_dish()
        self._builder.add_drink()
        
        return self._builder.get_meal()
    
    def construct_standard_meal(self, name: str = None, price: float = None) -> Meal:
        """
        Construct a standard meal with main dish, side dish, and drink.
        
        Args:
            name: Optional name for the meal
            price: Optional price for the meal
            
        Returns:
            Meal: The constructed meal
            
        Raises:
            ValueError: If no builder is set
        """
        if not self._builder:
            raise ValueError("No builder set. Use set_builder() to set a builder.")
        
        self._builder.reset()
        
        if name:
            self._builder.set_name(name)
        
        if price:
            self._builder.set_price(price)
            
        self._builder.add_main_dish()
        self._builder.add_side_dish()
        self._builder.add_drink()
        
        return self._builder.get_meal()
    
    def construct_premium_meal(self, name: str = None, price: float = None, description: str = None) -> Meal:
        """
        Construct a premium meal with all available components.
        
        Args:
            name: Optional name for the meal
            price: Optional price for the meal
            description: Optional description for the meal
            
        Returns:
            Meal: The constructed meal
            
        Raises:
            ValueError: If no builder is set
        """
        if not self._builder:
            raise ValueError("No builder set. Use set_builder() to set a builder.")
        
        self._builder.reset()
        
        if name:
            self._builder.set_name(name)
        
        if description:
            self._builder.set_description(description)
        
        if price:
            self._builder.set_price(price)
            
        self._builder.add_appetizer()
        self._builder.add_main_dish()
        self._builder.add_side_dish()
        self._builder.add_drink()
        self._builder.add_dessert()
        self._builder.add_extras()
        self._builder.add_nutrition_info()
        
        return self._builder.get_meal()
    
    def construct_custom_meal(self, config: MealConfig) -> Meal:
        """
        Construct a custom meal based on the provided configuration.
        
        Args:
            config: A MealConfig object specifying which components to include
            
        Returns:
            Meal: The constructed meal
            
        Raises:
            ValueError: If no builder is set
        """
        if not self._builder:
            raise ValueError("No builder set. Use set_builder() to set a builder.")
        
        self._builder.reset()
        
        if config.name:
            self._builder.set_name(config.name)
        
        if config.description:
            self._builder.set_description(config.description)
        
        if config.price:
            self._builder.set_price(config.price)
        
        if config.appetizer:
            self._builder.add_appetizer()
            
        if config.main_dish:
            self._builder.add_main_dish()
            
        if config.side_dish:
            self._builder.add_side_dish()
            
        if config.drink:
            self._builder.add_drink()
            
        if config.dessert:
            self._builder.add_dessert()
            
        if config.extras:
            self._builder.add_extras()
            
        if config.nutrition_info:
            self._builder.add_nutrition_info()
        
        return self._builder.get_meal()
    
    # Backward compatibility method for dictionary-based config
    def construct_meal_from_dict(self, config: Dict[str, Any]) -> Meal:
        """
        Legacy method to construct a meal from a dictionary configuration.
        
        This method converts a dictionary configuration to a MealConfig object
        and delegates to construct_custom_meal.
        
        Args:
            config: A dictionary with configuration options
            
        Returns:
            Meal: The constructed meal
        """
        meal_config = MealConfig(
            name=config.get("name"),
            description=config.get("description"),
            price=config.get("price"),
            main_dish=config.get("main_dish", False),
            side_dish=config.get("side_dish", False),
            drink=config.get("drink", False),
            dessert=config.get("dessert", False),
            appetizer=config.get("appetizer", False),
            extras=config.get("extras", False),
            nutrition_info=config.get("nutrition_info", False),
            nutrition_values=config.get("nutrition_values")
        )
        
        return self.construct_custom_meal(meal_config) 