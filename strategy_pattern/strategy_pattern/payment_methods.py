"""Payment method implementations."""

from decimal import Decimal
from typing import Dict
from strategy_pattern.payment_strategy import PaymentStrategy


class CreditCardPayment(PaymentStrategy):
    """Credit card payment implementation."""

    def __init__(self, card_number: str, expiry_date: str, cvv: str) -> None:
        """
        Initialize credit card payment.

        Args:
            card_number: The credit card number
            expiry_date: The card expiry date (MM/YY)
            cvv: The card CVV code
        """
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def pay(self, amount: Decimal) -> bool:
        """
        Process a credit card payment.

        Args:
            amount: The payment amount

        Returns:
            True if payment was successful, False otherwise
        """
        # In a real implementation, this would integrate with a payment gateway
        print(
            f"Processing credit card payment of ${amount:.2f} "
            f"with card ending in {self.card_number[-4:]}"
        )
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
        # In a real implementation, this would use the PayPal API
        print(f"Processing PayPal payment of ${amount:.2f} from {self.email}")
        return True


class CryptoPayment(PaymentStrategy):
    """Cryptocurrency payment implementation."""

    def __init__(self, wallet_address: str, currency: str = "BTC") -> None:
        """
        Initialize cryptocurrency payment.

        Args:
            wallet_address: The cryptocurrency wallet address
            currency: The cryptocurrency code (default: BTC)
        """
        self.wallet_address = wallet_address
        self.currency = currency.upper()

    def pay(self, amount: Decimal) -> bool:
        """
        Process a cryptocurrency payment.

        Args:
            amount: The payment amount in USD

        Returns:
            True if payment was successful, False otherwise
        """
        # Mock exchange rates for demonstration
        exchange_rates: Dict[str, Decimal] = {
            "BTC": Decimal("30000.00"),
            "ETH": Decimal("2000.00"),
            "DOGE": Decimal("0.10"),
        }

        if self.currency not in exchange_rates:
            print(f"Unsupported cryptocurrency: {self.currency}")
            return False

        crypto_amount = amount / exchange_rates[self.currency]
        print(
            f"Processing {self.currency} payment of {crypto_amount:.8f} "
            f"(${amount:.2f} USD) to {self.wallet_address}"
        )
        return True
