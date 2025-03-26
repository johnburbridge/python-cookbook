#!/usr/bin/env python3
"""
Demonstrates the Strategy Pattern with different payment methods.
"""
from strategy_pattern.shopping_cart import ShoppingCart
from strategy_pattern.payment_methods import CreditCardPayment, PayPalPayment, BitcoinPayment

def main():
    """
    Main function to demonstrate the Strategy Pattern.
    """
    # Create a shopping cart
    cart = ShoppingCart()
    
    # Add some items to the cart
    cart.add_item("1", "Laptop", 1299.99)
    cart.add_item("2", "Mouse", 25.50, 2)
    cart.add_item("3", "Headphones", 199.99)
    
    # Calculate and display the total
    total = cart.calculate_total()
    print(f"Cart total: ${total:.2f}")
    
    # Prompt the user to choose a payment method
    print("\nChoose a payment method:")
    print("1. Credit Card")
    print("2. PayPal")
    print("3. Bitcoin")
    
    choice = input("Enter your choice (1-3): ")
    
    # Set the payment strategy based on the user's choice
    if choice == "1":
        card_number = input("Enter your credit card number: ")
        expiry_date = input("Enter the expiry date (MM/YY): ")
        cvv = input("Enter the CVV: ")
        name = input("Enter the cardholder name: ")
        payment_strategy = CreditCardPayment(card_number, expiry_date, cvv, name)
    elif choice == "2":
        email = input("Enter your PayPal email: ")
        password = input("Enter your PayPal password: ")
        payment_strategy = PayPalPayment(email, password)
    elif choice == "3":
        wallet = input("Enter your Bitcoin wallet address: ")
        payment_strategy = BitcoinPayment(wallet)
    else:
        print("Invalid choice. Exiting.")
        return
    
    # Set the payment strategy and checkout
    cart.set_payment_strategy(payment_strategy)
    success = cart.checkout()
    
    if success:
        print("Thank you for your purchase!")
    else:
        print("Sorry, there was an issue with your payment. Please try again.")

if __name__ == "__main__":
    main() 