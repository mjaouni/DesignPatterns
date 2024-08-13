from abc import ABC, abstractmethod


# Visitor Interface
class Visitor(ABC):
    def visit_food(self, food_item: 'MenuItem'):
        pass

    def visit_beverage(self, beverage_item: 'MenuItem'):
        pass

    def visit_dessert(self, dessert_item: 'MenuItem'):
        pass


# Concrete Visitor
class BillVisitor(Visitor):
    def __init__(self):
        self.total = 0

    def visit_food(self, food_item: 'MenuItem'):
        self.total += food_item.price

    def visit_beverage(self, beverage_item: 'MenuItem'):
        self.total += beverage_item.price

    def visit_dessert(self, visit_dessert: 'MenuItem'):
        self.total += visit_dessert.price

    def get_total(self):
        return self.total


class CalorieVisitor(Visitor):
    def __init__(self):
        self.total_calories = 0

    def visit_food(self, food_item: 'MenuItem'):
        self.total_calories += food_item.calories

    def visit_beverage(self, beverage_item: 'MenuItem'):
        self.total_calories += beverage_item.calories

    def visit_dessert(self, visit_dessert: 'MenuItem'):
        self.total_calories += visit_dessert.calories

    def get_total_calories(self):
        return self.total_calories


# Element Interface
class MenuItem(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


# Concreate Classes
class Food(MenuItem):
    def __init__(self, name, price, calories):
        self.name = name
        self.price = price
        self.calories = calories

    def accept(self, visitor: Visitor):
        visitor.visit_food(self)


class Beverage(MenuItem):
    def __init__(self, name, price, calories):
        self.name = name
        self.price = price
        self.calories = calories

    def accept(self, visitor: Visitor):
        visitor.visit_beverage(self)


class Dessert(MenuItem):
    def __init__(self, name, price, calories):
        self.name = name
        self.price = price
        self.calories = calories

    def accept(self, visitor: Visitor):
        visitor.visit_dessert(self)


# Usage

pizza = Food("Pizza", 10, 800)
coffee = Beverage("Coffee", 5, 100)
cake = Dessert("Cake", 7, 500)

# List of Menu Item
menu_items = [pizza, coffee, cake]

bill_visitor = BillVisitor()
for item in menu_items:
    item.accept(bill_visitor)

print(f"Total bill: ${bill_visitor.get_total()}")

calorie_visitor = CalorieVisitor()
for item in menu_items:
    item.accept(calorie_visitor)

print(f"Total calories: {calorie_visitor.get_total_calories()} kcal")
