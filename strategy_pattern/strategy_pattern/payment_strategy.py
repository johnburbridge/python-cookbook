"""Payment strategy interface."""

from abc import ABC, abstractmethod
from decimal import Decimal


class PaymentStrategy(ABC):
    """Abstract base class for payment strategies."""

    @abstractmethod
    def pay(self, amount: Decimal) -> bool:
        """
        Process a payment.

        Args:
            amount: The payment amount

        Returns:
            True if payment was successful, False otherwise
        """
        pass
