import unittest
from unittest.mock import patch
from io import StringIO

from strategy_pattern.shopping_cart import ShoppingCart
from strategy_pattern.payment_methods import (
    CreditCardPayment,
    PayPalPayment,
    BitcoinPayment,
)


class TestPaymentStrategies(unittest.TestCase):
    """
    Test cases for the payment strategies implementation.
    """

    def setUp(self):
        """
        Set up a new shopping cart for each test.
        """
        self.cart = ShoppingCart()
        self.cart.add_item("1", "Test Item", 10.00, 2)

    def test_credit_card_payment(self):
        """
        Test credit card payment strategy.
        """
        # Create a credit card payment strategy
        credit_card = CreditCardPayment("1234567890123456", "12/25", "123", "John Doe")

        # Test that the credit card number is properly masked
        self.assertEqual(credit_card._mask_card_number(), "************3456")

        # Set the payment strategy and check out
        self.cart.set_payment_strategy(credit_card)

        # Capture the printed output
        with patch("sys.stdout", new=StringIO()) as fake_output:
            result = self.cart.checkout()
            output = fake_output.getvalue()

        # Check that the payment was successful
        self.assertTrue(result)
        self.assertIn("Processing credit card payment", output)
        self.assertIn("Card Number: ************3456", output)
        self.assertIn("Card Holder: John Doe", output)
        self.assertIn("Payment successful!", output)

    def test_paypal_payment(self):
        """
        Test PayPal payment strategy.
        """
        # Create a PayPal payment strategy
        paypal = PayPalPayment("test@example.com", "password123")

        # Set the payment strategy and check out
        self.cart.set_payment_strategy(paypal)

        # Capture the printed output
        with patch("sys.stdout", new=StringIO()) as fake_output:
            result = self.cart.checkout()
            output = fake_output.getvalue()

        # Check that the payment was successful
        self.assertTrue(result)
        self.assertIn("Processing PayPal payment", output)
        self.assertIn("PayPal Account: test@example.com", output)
        self.assertIn("Payment successful!", output)

    def test_bitcoin_payment(self):
        """
        Test Bitcoin payment strategy.
        """
        # Create a Bitcoin payment strategy
        bitcoin = BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")

        # Set the payment strategy and check out
        self.cart.set_payment_strategy(bitcoin)

        # Capture the printed output
        with patch("sys.stdout", new=StringIO()) as fake_output:
            result = self.cart.checkout()
            output = fake_output.getvalue()

        # Check that the payment was successful
        self.assertTrue(result)
        self.assertIn("Processing Bitcoin payment", output)
        self.assertIn("Bitcoin Wallet: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", output)
        self.assertIn("Payment successful!", output)

    def test_no_payment_strategy(self):
        """
        Test checkout with no payment strategy set.
        """
        # Capture the printed output
        with patch("sys.stdout", new=StringIO()) as fake_output:
            result = self.cart.checkout()
            output = fake_output.getvalue()

        # Check that the payment failed
        self.assertFalse(result)
        self.assertIn("No payment strategy set.", output)

    def test_empty_cart(self):
        """
        Test checkout with an empty cart.
        """
        # Empty the cart
        self.cart.items.clear()

        # Set a payment strategy
        self.cart.set_payment_strategy(
            CreditCardPayment("1234567890123456", "12/25", "123", "John Doe")
        )

        # Capture the printed output
        with patch("sys.stdout", new=StringIO()) as fake_output:
            result = self.cart.checkout()
            output = fake_output.getvalue()

        # Check that the payment failed
        self.assertFalse(result)
        self.assertIn("Shopping cart is empty.", output)

    def test_remove_item(self):
        """
        Test removing items from the cart.
        """
        # Add another item
        self.cart.add_item("2", "Another Item", 15.00, 3)

        # Remove one of the first item
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.cart.remove_item("1", 1)
            output = fake_output.getvalue()

        self.assertIn("Removed 1 x Test Item from cart", output)
        self.assertEqual(self.cart.items["1"]["quantity"], 1)

        # Remove all of the first item
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.cart.remove_item("1", 1)
            output = fake_output.getvalue()

        self.assertIn("Removed Test Item from cart", output)
        self.assertNotIn("1", self.cart.items)

        # Try to remove a non-existent item
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.cart.remove_item("3")
            output = fake_output.getvalue()

        self.assertIn("Item 3 not in cart", output)

    def test_calculate_total(self):
        """
        Test calculating the total price of items in the cart.
        """
        # Add another item
        self.cart.add_item("2", "Another Item", 15.00, 3)

        # Calculate the expected total
        expected_total = (10.00 * 2) + (15.00 * 3)

        # Check that the calculated total matches the expected total
        self.assertEqual(self.cart.calculate_total(), expected_total)


if __name__ == "__main__":
    unittest.main()
