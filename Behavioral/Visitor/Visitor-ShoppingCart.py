from abc import ABC, abstractmethod


# Visitor Interface
class ShoppingCartVisitor(ABC):
    @abstractmethod
    def visit_electronics(self, electronics_item: 'Product'):
        pass

    @abstractmethod
    def visit_book(self, book_item: 'Product'):
        pass

    @abstractmethod
    def visit_clothing(self, clothing_item: 'Product'):
        pass


# Concrete Visitor for calculating total price
class PriceCalculateVisitor(ShoppingCartVisitor):
    def __init__(self):
        self.total_price = 0

    def visit_electronics(self, electronics_item: 'Product'):
        self.total_price += electronics_item.price

    def visit_book(self, book_item: 'Product'):
        self.total_price += book_item.price

    def visit_clothing(self, clothing_item: 'Product'):
        self.total_price += clothing_item.price

    def get_total_price(self):
        return self.total_price


# Concreate Visitor for applying discount
class DiscountVisitor(ShoppingCartVisitor):
    def __init__(self):
        self.discount_price = 0

    def visit_electronics(self, electronics_item: 'Product'):
        self.discount_price += electronics_item.price * 0.9  # 10% discount

    def visit_book(self, book_item: 'Product'):
        self.discount_price += book_item.price * 0.95  # 5% discount

    def visit_clothing(self, clothing_item: 'Product'):
        self.discount_price += clothing_item.price * 0.8  # 20% discount

    def get_discounted_price(self):
        return self.discount_price


# Element Interface
class Product(ABC):
    @abstractmethod
    def accept(self, visitor: ShoppingCartVisitor):
        pass


# Concreate Elements
class Electronics(Product):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def accept(self, visitor: ShoppingCartVisitor):
        visitor.visit_electronics(self)


class Book(Product):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def accept(self, visitor: ShoppingCartVisitor):
        visitor.visit_book(self)


class Clothing(Product):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def accept(self, visitor: ShoppingCartVisitor):
        visitor.visit_clothing(self)


# Usage

laptop = Electronics("Laptop", 1000)
novel = Book("Novel", 30)
tshirt = Clothing("T-shirt", 25)

# List of Products
products = [laptop, novel, tshirt]

# Calculate total price
price_calculator = PriceCalculateVisitor()

for product in products:
    product.accept(price_calculator)

print(f"Total Price: ${price_calculator.get_total_price()}")

# Apply discounts
discount_visitor = DiscountVisitor()

for product in products:
    product.accept(discount_visitor)

print(f"Discounted Price: ${discount_visitor.get_discounted_price()}")
