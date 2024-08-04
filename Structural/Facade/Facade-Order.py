# Subsystem Classes
class Inventory:
    def __init__(self):
        self.stock = {'item1': 10, 'item2': 3}

    def check_stock(self, item):
        if item in self.stock and self.stock[item] > 0:
            return True
        return False

    def reduce_stock(self, item):
        if self.stock[item]:
            self.stock[item] -= 1
            print(f'The Stock for {item} reduced by one.Remaining: {self.stock[item]}')
        else:
            print(f'Item {item} is out of Stock')


class Payment:
    @staticmethod
    def process_payment(amount):
        print(f'Processing payment of amount {amount}')
        return True


class Shipping:
    @staticmethod
    def arrange_shipping(item):
        print(f'Shipping arranged for item {item}')


# Facade Class
class OnlineShoppingFacade:
    def __init__(self):
        self.inventory = Inventory()
        self.payment = Payment()
        self.shipping = Shipping()

    def place_order(self, item, amount):

        print(f"Placing order for {item}")

        if not self.inventory.check_stock(item):
            print(f'Item {item} out of Stock')
            return False

        if not self.payment.process_payment(amount):
            # Process payment
            if not self.payment.process_payment(amount):
                print(f"Payment for {item} failed!")
                return False

        # Reduce item by one
        self.inventory.reduce_stock(item)

        # Arrange Shipping
        self.shipping.arrange_shipping(item)

        print(f"Order for {item} has been placed successfully!")
        return True


# Usage
order = OnlineShoppingFacade()
order.place_order('item1', 50)
order.place_order('item2', 110)
order.place_order('item2', 110)
order.place_order('item2', 110)
order.place_order('item2', 110)  # Out of Stock
