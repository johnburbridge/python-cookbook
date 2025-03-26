from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    """
    Strategy interface that declares the method all concrete payment strategies must implement.
    """

    @abstractmethod
    def pay(self, amount: float) -> bool:
        """
        Process a payment of the given amount.

        Args:
            amount: The amount to pay in the appropriate currency.

        Returns:
            bool: True if payment was successful, False otherwise.
        """
        pass
