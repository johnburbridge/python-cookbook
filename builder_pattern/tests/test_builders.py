import unittest

from builder_pattern.meal import Meal, MealItem
from builder_pattern.concrete_builders import RegularMealBuilder, VegetarianMealBuilder, ChildrenMealBuilder
from builder_pattern.meal_director import MealDirector, MealConfig
from builder_pattern.fluent_builder import FluentMealBuilder


class TestBuilderPattern(unittest.TestCase):
    """
    Test cases for the Builder Pattern implementation.
    """
    
    def test_regular_meal_builder(self):
        """
        Test the RegularMealBuilder
        """
        # Create a builder
        builder = RegularMealBuilder()
        
        # Reset and build a meal step by step
        builder.reset()
        builder.set_name("Test Regular Meal")
        builder.set_description("A test meal")
        builder.set_price(10.99)
        builder.add_main_dish()
        builder.add_side_dish()
        builder.add_drink()
        builder.add_dessert()
        builder.add_nutrition_info()
        
        # Get the meal
        meal = builder.get_meal()
        
        # Check the meal properties
        self.assertEqual(meal.name, "Test Regular Meal")
        self.assertEqual(meal.description, "A test meal")
        self.assertEqual(meal.price, 10.99)
        self.assertEqual(meal.main_dish, MealItem.BURGER)
        self.assertEqual(meal.side_dish, MealItem.FRIES)
        self.assertEqual(meal.drink, MealItem.SOFT_DRINK)
        self.assertEqual(meal.dessert, MealItem.ICE_CREAM)
        self.assertIn("Gluten", meal.contains_allergens)
        self.assertIn("Dairy", meal.contains_allergens)
        self.assertEqual(meal.total_items(), 4)  # main, side, drink, dessert
    
    def test_vegetarian_meal_builder(self):
        """
        Test the VegetarianMealBuilder
        """
        # Create a builder
        builder = VegetarianMealBuilder()
        
        # Reset and build a meal step by step
        builder.reset()
        builder.set_name("Test Vegetarian Meal")
        builder.set_price(12.99)
        builder.add_main_dish()
        builder.add_side_dish()
        builder.add_drink()
        builder.add_dessert()
        builder.add_extras()
        
        # Get the meal
        meal = builder.get_meal()
        
        # Check the meal properties
        self.assertEqual(meal.name, "Test Vegetarian Meal")
        self.assertEqual(meal.price, 12.99)
        self.assertEqual(meal.main_dish, MealItem.PASTA)
        self.assertEqual(meal.side_dish, MealItem.SALAD)
        self.assertEqual(meal.drink, MealItem.JUICE)
        self.assertEqual(meal.dessert, MealItem.FRUIT)
        self.assertEqual(meal.extras, [MealItem.SALAD])  # Extra veggies
        self.assertTrue(meal.is_vegetarian)
        self.assertIn("Gluten", meal.contains_allergens)
        self.assertEqual(meal.total_items(), 5)  # main, side, drink, dessert, 1 extra
    
    def test_children_meal_builder(self):
        """
        Test the ChildrenMealBuilder
        """
        # Create a builder
        builder = ChildrenMealBuilder()
        
        # Reset and build a meal step by step
        builder.reset()
        builder.set_name("Test Kids Meal")
        builder.set_price(7.99)
        builder.add_main_dish()
        builder.add_side_dish()
        builder.add_drink()
        builder.add_dessert()
        builder.add_extras()
        
        # Get the meal
        meal = builder.get_meal()
        
        # Check the meal properties
        self.assertEqual(meal.name, "Test Kids Meal")
        self.assertEqual(meal.price, 7.99)
        self.assertEqual(meal.main_dish, MealItem.CHICKEN)
        self.assertEqual(meal.side_dish, MealItem.FRIES)
        self.assertEqual(meal.drink, MealItem.JUICE)
        self.assertEqual(meal.dessert, MealItem.ICE_CREAM)
        self.assertEqual(meal.extras, [MealItem.TOY])
        self.assertTrue(meal.is_kids_meal)
        self.assertIn("Dairy", meal.contains_allergens)
        self.assertEqual(meal.total_items(), 5)  # main, side, drink, dessert, toy
    
    def test_meal_director(self):
        """
        Test the MealDirector with different builders
        """
        # Create builders
        regular_builder = RegularMealBuilder()
        vegetarian_builder = VegetarianMealBuilder()
        
        # Create director
        director = MealDirector()
        
        # Test with no builder
        with self.assertRaises(ValueError):
            director.construct_basic_meal()
        
        # Set regular builder and test basic meal
        director.set_builder(regular_builder)
        basic_meal = director.construct_basic_meal(name="Basic Test", price=8.99)
        
        self.assertEqual(basic_meal.name, "Basic Test")
        self.assertEqual(basic_meal.price, 8.99)
        self.assertEqual(basic_meal.main_dish, MealItem.BURGER)
        self.assertEqual(basic_meal.drink, MealItem.SOFT_DRINK)
        self.assertIsNone(basic_meal.side_dish)
        self.assertEqual(basic_meal.total_items(), 2)  # main, drink
        
        # Test standard meal
        standard_meal = director.construct_standard_meal()
        self.assertEqual(standard_meal.main_dish, MealItem.BURGER)
        self.assertEqual(standard_meal.side_dish, MealItem.FRIES)
        self.assertEqual(standard_meal.drink, MealItem.SOFT_DRINK)
        self.assertEqual(standard_meal.total_items(), 3)  # main, side, drink
        
        # Switch to vegetarian builder and test premium meal
        director.set_builder(vegetarian_builder)
        premium_meal = director.construct_premium_meal(
            name="Premium Test",
            price=15.99,
            description="Premium test meal"
        )
        
        self.assertEqual(premium_meal.name, "Premium Test")
        self.assertEqual(premium_meal.price, 15.99)
        self.assertEqual(premium_meal.description, "Premium test meal")
        self.assertEqual(premium_meal.main_dish, MealItem.PASTA)
        self.assertEqual(premium_meal.side_dish, MealItem.SALAD)
        self.assertEqual(premium_meal.appetizer, MealItem.SOUP)
        self.assertEqual(premium_meal.drink, MealItem.JUICE)
        self.assertEqual(premium_meal.dessert, MealItem.FRUIT)
        self.assertTrue(premium_meal.is_vegetarian)
        self.assertEqual(premium_meal.total_items(), 6)  # main, side, drink, dessert, appetizer, 1 extra
        
        # Test custom configuration with MealConfig
        custom_config = MealConfig(
            name="Custom Test",
            price=9.99,
            main_dish=True,
            drink=True
        )
        custom_meal = director.construct_custom_meal(custom_config)
        
        self.assertEqual(custom_meal.name, "Custom Test")
        self.assertEqual(custom_meal.price, 9.99)
        self.assertEqual(custom_meal.main_dish, MealItem.PASTA)
        self.assertEqual(custom_meal.drink, MealItem.JUICE)
        self.assertIsNone(custom_meal.side_dish)
        self.assertTrue(custom_meal.is_vegetarian)
        self.assertEqual(custom_meal.total_items(), 2)  # main, drink
        
        # Test backwards compatibility with dictionary-based config
        dict_config = {
            "name": "Dict Config Test",
            "price": 10.99,
            "main_dish": True,
            "side_dish": True
        }
        dict_meal = director.construct_meal_from_dict(dict_config)
        
        self.assertEqual(dict_meal.name, "Dict Config Test")
        self.assertEqual(dict_meal.price, 10.99)
        self.assertEqual(dict_meal.main_dish, MealItem.PASTA)
        self.assertEqual(dict_meal.side_dish, MealItem.SALAD)
        self.assertTrue(dict_meal.is_vegetarian)
        self.assertEqual(dict_meal.total_items(), 2)  # main, side
    
    def test_fluent_builder(self):
        """
        Test the FluentMealBuilder
        """
        # Create a meal with the fluent builder
        meal = (
            FluentMealBuilder()
            .with_name("Fluent Test Meal")
            .with_description("A test meal created with the fluent builder")
            .with_price(13.99)
            .with_main_dish(MealItem.FISH)
            .with_side_dish(MealItem.RICE)
            .with_drink(MealItem.WATER)
            .with_dessert(MealItem.CAKE)
            .with_allergen("Fish")
            .with_nutrition_info({
                "calories": 800,
                "protein": 40,
                "carbs": 60,
                "fat": 25
            })
            .build()
        )
        
        # Check the meal properties
        self.assertEqual(meal.name, "Fluent Test Meal")
        self.assertEqual(meal.description, "A test meal created with the fluent builder")
        self.assertEqual(meal.price, 13.99)
        self.assertEqual(meal.main_dish, MealItem.FISH)
        self.assertEqual(meal.side_dish, MealItem.RICE)
        self.assertEqual(meal.drink, MealItem.WATER)
        self.assertEqual(meal.dessert, MealItem.CAKE)
        self.assertIn("Fish", meal.contains_allergens)
        self.assertIn("Dairy", meal.contains_allergens)  # From cake
        self.assertEqual(meal.nutrition_info["calories"], 800)
        self.assertEqual(meal.total_items(), 4)  # main, side, drink, dessert
        
        # Test fluent builder with vegetarian and kids meal flags
        kids_vegetarian_meal = (
            FluentMealBuilder()
            .with_name("Kids Vegetarian")
            .with_price(8.99)
            .with_main_dish(MealItem.PASTA)
            .with_drink(MealItem.JUICE)
            .vegetarian()
            .kids_meal()
            .with_extras([MealItem.TOY])
            .build()
        )
        
        self.assertEqual(kids_vegetarian_meal.name, "Kids Vegetarian")
        self.assertEqual(kids_vegetarian_meal.price, 8.99)
        self.assertEqual(kids_vegetarian_meal.main_dish, MealItem.PASTA)
        self.assertEqual(kids_vegetarian_meal.drink, MealItem.JUICE)
        self.assertEqual(kids_vegetarian_meal.extras, [MealItem.TOY])
        self.assertTrue(kids_vegetarian_meal.is_vegetarian)
        self.assertTrue(kids_vegetarian_meal.is_kids_meal)
        self.assertIn("Gluten", kids_vegetarian_meal.contains_allergens)
        self.assertEqual(kids_vegetarian_meal.total_items(), 3)  # main, drink, toy
    
    def test_meal_display(self):
        """
        Test the display method of Meal
        """
        meal = Meal(
            name="Display Test Meal",
            description="A test meal for displaying",
            price=12.99,
            main_dish=MealItem.BURGER,
            side_dish=MealItem.FRIES,
            drink=MealItem.SOFT_DRINK,
            dessert=MealItem.ICE_CREAM,
            extras=[MealItem.TOY],
            is_kids_meal=True,
            contains_allergens=["Gluten", "Dairy"]
        )
        
        display_output = meal.display()
        
        # Check that the display output contains all the meal information
        self.assertIn("=== Display Test Meal ===", display_output)
        self.assertIn("A test meal for displaying", display_output)
        self.assertIn("Price: $12.99", display_output)
        self.assertIn("Main: Burger", display_output)
        self.assertIn("Side: Fries", display_output)
        self.assertIn("Drink: Soft Drink", display_output)
        self.assertIn("Dessert: Ice Cream", display_output)
        self.assertIn("Extras: Toy", display_output)
        self.assertIn("Kids Meal: Yes", display_output)
        self.assertIn("Allergens: Gluten, Dairy", display_output)
    
    def test_meal_total_items(self):
        """
        Test the total_items method of Meal
        """
        # Create an empty meal
        empty_meal = Meal(name="Empty Meal")
        self.assertEqual(empty_meal.total_items(), 0)
        
        # Create a meal with only a main dish
        main_dish_meal = Meal(name="Main Dish Meal", main_dish=MealItem.BURGER)
        self.assertEqual(main_dish_meal.total_items(), 1)
        
        # Create a meal with all items
        full_meal = Meal(
            name="Full Meal",
            main_dish=MealItem.BURGER,
            side_dish=MealItem.FRIES,
            drink=MealItem.SOFT_DRINK,
            dessert=MealItem.ICE_CREAM,
            appetizer=MealItem.SALAD,
            extras=[MealItem.TOY, MealItem.FRUIT]
        )
        self.assertEqual(full_meal.total_items(), 7)  # main, side, drink, dessert, appetizer, 2 extras


if __name__ == "__main__":
    unittest.main() 