from strategy_pattern.payment_strategy import PaymentStrategy

class CreditCardPayment(PaymentStrategy):
    """
    Concrete strategy for credit card payments.
    """
    def __init__(self, card_number: str, expiry_date: str, cvv: str, card_holder_name: str):
        """
        Initialize with credit card details.
        
        Args:
            card_number: The credit card number.
            expiry_date: The expiry date of the card.
            cvv: The CVV code.
            card_holder_name: The name of the card holder.
        """
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv
        self.card_holder_name = card_holder_name
        
    def pay(self, amount: float) -> bool:
        """
        Process credit card payment.
        
        Args:
            amount: The amount to charge to the credit card.
            
        Returns:
            bool: True if payment was successful, False otherwise.
        """
        print(f"Processing credit card payment of ${amount:.2f}")
        print(f"Card Number: {self._mask_card_number()}")
        print(f"Card Holder: {self.card_holder_name}")
        print(f"Expiry Date: {self.expiry_date}")
        # In a real implementation, this would communicate with a payment gateway
        return True
    
    def _mask_card_number(self) -> str:
        """
        Masks the credit card number for security purposes.
        
        Returns:
            str: The masked credit card number.
        """
        return "*" * (len(self.card_number) - 4) + self.card_number[-4:]


class PayPalPayment(PaymentStrategy):
    """
    Concrete strategy for PayPal payments.
    """
    def __init__(self, email: str, password: str):
        """
        Initialize with PayPal credentials.
        
        Args:
            email: The PayPal account email.
            password: The PayPal account password.
        """
        self.email = email
        self.password = password
        
    def pay(self, amount: float) -> bool:
        """
        Process PayPal payment.
        
        Args:
            amount: The amount to charge to the PayPal account.
            
        Returns:
            bool: True if payment was successful, False otherwise.
        """
        print(f"Processing PayPal payment of ${amount:.2f}")
        print(f"PayPal Account: {self.email}")
        # In a real implementation, this would use the PayPal API
        return True


class BitcoinPayment(PaymentStrategy):
    """
    Concrete strategy for Bitcoin payments.
    """
    def __init__(self, wallet_address: str):
        """
        Initialize with Bitcoin wallet address.
        
        Args:
            wallet_address: The Bitcoin wallet address.
        """
        self.wallet_address = wallet_address
        
    def pay(self, amount: float) -> bool:
        """
        Process Bitcoin payment.
        
        Args:
            amount: The amount in USD to convert to Bitcoin and charge.
            
        Returns:
            bool: True if payment was successful, False otherwise.
        """
        # In a real implementation, this would convert USD to BTC using current exchange rate
        btc_amount = amount / 50000  # Using a fixed exchange rate for simplicity
        print(f"Processing Bitcoin payment of ${amount:.2f} (BTC {btc_amount:.8f})")
        print(f"Bitcoin Wallet: {self.wallet_address}")
        # In a real implementation, this would create a Bitcoin transaction
        return True 