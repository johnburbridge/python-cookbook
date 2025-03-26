from typing import Dict, Optional
from strategy_pattern.payment_strategy import PaymentStrategy


class ShoppingCart:
    """
    Context class that uses a payment strategy to process payments.
    """

    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.items: Dict[str, Dict[str, float]] = {}
        self.payment_strategy: Optional[PaymentStrategy] = None

    def add_item(
        self, item_id: str, name: str, price: float, quantity: int = 1
    ) -> None:
        """
        Add an item to the shopping cart.

        Args:
            item_id: Unique identifier for the item.
            name: Name of the item.
            price: Price of the item.
            quantity: Quantity of the item to add (default is 1).
        """
        if item_id in self.items:
            self.items[item_id]["quantity"] += quantity
        else:
            self.items[item_id] = {"name": name, "price": price, "quantity": quantity}
        print(f"Added {quantity} x {name} to cart.")

    def remove_item(self, item_id: str, quantity: int = 1) -> None:
        """
        Remove an item from the shopping cart.

        Args:
            item_id: Unique identifier for the item.
            quantity: Quantity of the item to remove (default is 1).
        """
        if item_id not in self.items:
            print(f"Item {item_id} not in cart.")
            return

        if self.items[item_id]["quantity"] <= quantity:
            item_name = self.items[item_id]["name"]  # Store name before deleting
            del self.items[item_id]
            print(f"Removed {item_name} from cart.")
        else:
            self.items[item_id]["quantity"] -= quantity
            print(f"Removed {quantity} x {self.items[item_id]['name']} from cart.")

    def calculate_total(self) -> float:
        """
        Calculate the total price of all items in the cart.

        Returns:
            float: The total price.
        """
        total = 0.0
        for item in self.items.values():
            total += item["price"] * item["quantity"]
        return total

    def set_payment_strategy(self, payment_strategy: PaymentStrategy) -> None:
        """
        Set the payment strategy to use.

        Args:
            payment_strategy: The payment strategy to use.
        """
        self.payment_strategy = payment_strategy

    def checkout(self) -> bool:
        """
        Process the payment for the items in the cart.

        Returns:
            bool: True if payment was successful, False otherwise.
        """
        if not self.items:
            print("Shopping cart is empty.")
            return False

        if not self.payment_strategy:
            print("No payment strategy set.")
            return False

        total = self.calculate_total()
        print(f"Checking out {len(self.items)} items:")
        for item in self.items.values():
            print(f"  {item['quantity']} x {item['name']} - ${item['price']:.2f} each")
        print(f"Total: ${total:.2f}")

        if self.payment_strategy.pay(total):
            print("Payment successful!")
            self.items.clear()
            return True
        else:
            print("Payment failed!")
            return False
