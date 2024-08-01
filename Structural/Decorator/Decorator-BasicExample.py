from abc import ABC, abstractmethod


# Abstract class
class Beverage(ABC):
    def get_description(self) -> str:
        pass

    def cost(self) -> float:
        pass


# Concreate Beverage
class Espresso(Beverage):
    def get_description(self) -> str:
        return "Espresso"

    def cost(self) -> float:
        return 1.99


# Abstract Decorator
class Decorator(Beverage):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description()

    def cost(self) -> float:
        return self.beverage.cost()


# Concrete Decorator
class Mocha(Decorator):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage)

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Mocha"

    def cost(self) -> float:
        return self.beverage.cost() + 0.20


# Concrete Decorator
class Whip(Decorator):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage)

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Whip"

    def cost(self) -> float:
        return self.beverage.cost() + 0.10


beverage = Espresso()
print(beverage.get_description())
print(beverage.cost())

beverage = Mocha(Espresso())
beverage = Whip(beverage)
print(beverage.get_description())
print(beverage.cost())
