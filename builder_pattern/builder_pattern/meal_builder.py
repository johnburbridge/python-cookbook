from abc import ABC, abstractmethod
from builder_pattern.meal import Meal


class MealBuilder(ABC):
    """
    The abstract builder interface that defines all the steps to build a meal.
    """
    
    @abstractmethod
    def reset(self) -> None:
        """
        Reset the builder to create a new meal.
        """
        pass
    
    @abstractmethod
    def set_name(self, name: str) -> None:
        """
        Set the name of the meal.
        
        Args:
            name: The name of the meal
        """
        pass
    
    @abstractmethod
    def set_description(self, description: str) -> None:
        """
        Set the description of the meal.
        
        Args:
            description: The description of the meal
        """
        pass
    
    @abstractmethod
    def set_price(self, price: float) -> None:
        """
        Set the price of the meal.
        
        Args:
            price: The price of the meal
        """
        pass
    
    @abstractmethod
    def add_main_dish(self) -> None:
        """
        Add a main dish to the meal.
        """
        pass
    
    @abstractmethod
    def add_side_dish(self) -> None:
        """
        Add a side dish to the meal.
        """
        pass
    
    @abstractmethod
    def add_drink(self) -> None:
        """
        Add a drink to the meal.
        """
        pass
    
    @abstractmethod
    def add_dessert(self) -> None:
        """
        Add a dessert to the meal.
        """
        pass
    
    @abstractmethod
    def add_appetizer(self) -> None:
        """
        Add an appetizer to the meal.
        """
        pass
    
    @abstractmethod
    def add_extras(self) -> None:
        """
        Add extras to the meal.
        """
        pass
    
    @abstractmethod
    def add_nutrition_info(self) -> None:
        """
        Add nutrition information to the meal.
        """
        pass
    
    @abstractmethod
    def get_meal(self) -> Meal:
        """
        Return the constructed meal.
        
        Returns:
            Meal: The constructed meal
        """
        pass 