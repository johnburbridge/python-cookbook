"""Payment method implementations."""

from decimal import Decimal
from strategy_pattern.payment_strategy import PaymentStrategy


class CreditCardPayment(PaymentStrategy):
    """Credit card payment implementation."""

    def __init__(
        self, card_number: str, expiry_date: str, cvv: str, card_holder: str
    ) -> None:
        """
        Initialize credit card payment.

        Args:
            card_number: The credit card number
            expiry_date: The card expiry date (MM/YY)
            cvv: The card CVV code
            card_holder: The name of the card holder
        """
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv
        self.card_holder = card_holder

    def _mask_card_number(self) -> str:
        """Mask the card number for display."""
        return "*" * 12 + self.card_number[-4:]

    def pay(self, amount: Decimal) -> bool:
        """
        Process a credit card payment.

        Args:
            amount: The payment amount

        Returns:
            True if payment was successful, False otherwise
        """
        print("Processing credit card payment")
        print(f"Card Number: {self._mask_card_number()}")
        print(f"Card Holder: {self.card_holder}")
        print("Payment successful!")
        return True


class PayPalPayment(PaymentStrategy):
    """PayPal payment implementation."""

    def __init__(self, email: str, password: str) -> None:
        """
        Initialize PayPal payment.

        Args:
            email: The PayPal account email
            password: The PayPal account password
        """
        self.email = email
        self.password = password

    def pay(self, amount: Decimal) -> bool:
        """
        Process a PayPal payment.

        Args:
            amount: The payment amount

        Returns:
            True if payment was successful, False otherwise
        """
        print("Processing PayPal payment")
        print(f"PayPal Account: {self.email}")
        print("Payment successful!")
        return True


class BitcoinPayment(PaymentStrategy):
    """Bitcoin payment implementation."""

    def __init__(self, wallet_address: str) -> None:
        """
        Initialize Bitcoin payment.

        Args:
            wallet_address: The Bitcoin wallet address
        """
        self.wallet_address = wallet_address

    def pay(self, amount: Decimal) -> bool:
        """
        Process a Bitcoin payment.

        Args:
            amount: The payment amount

        Returns:
            True if payment was successful, False otherwise
        """
        print("Processing Bitcoin payment")
        print(f"Bitcoin Wallet: {self.wallet_address}")
        print("Payment successful!")
        return True
