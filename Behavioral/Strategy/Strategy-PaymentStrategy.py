from abc import ABC, abstractmethod
from typing import Optional


# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


# Concrete Strategies
class CreditCardPayment(PaymentStrategy):

    def __init__(self, card_number: str, card_expiry: str, cvv: str):
        self.card_number = card_number
        self.card_expiry = card_expiry
        self.cvv = cvv

    def pay(self, amount: float) -> None:
        print(f'Paid {amount} using Credit Card ending in {self.card_number[-4:]}.')


class PayPalPayment(PaymentStrategy):

    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float) -> None:
        print(f'Paid {amount} using PayPal with email {self.email}')


class CryptoPayment(PaymentStrategy):

    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def pay(self, amount: float) -> None:
        print(f'Paid {amount} using Cryptocurrency with wallet {self.wallet_address}')


# Context Class
class ShoppingCard:
    def __init__(self):
        self.items = []
        self.payment_strategy: Optional[PaymentStrategy] = None

    def add_item(self, item: str, price: float):
        self.items.append((item, price))

    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def checkout(self):
        total = sum(price for item, price in self.items)
        if self.payment_strategy:
            self.payment_strategy.pay(total)
        else:
            print("Payment Strategy not set")


# Usage
cart = ShoppingCard()
cart.add_item("Laptop", 1200.00)
cart.add_item("Headphones", 200.00)

# Paying with a Credit Card
cart.set_payment_strategy(CreditCardPayment("1234567812345678", "12/28", "123"))
cart.checkout()

# Paying with PayPal
cart.set_payment_strategy(PayPalPayment('paypal@gmail.com'))
cart.checkout()

# Paying with Cryptocurrency
cart.set_payment_strategy(CryptoPayment('1A2B3C4D5E6F'))
cart.checkout()
