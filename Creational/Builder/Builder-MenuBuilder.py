from abc import ABC, abstractmethod


# Product class representing the object being built
class Menu:
    def __init__(self):
        self.main_course = None
        self.side_dish = None
        self.drink = None
        self.dessert = None

    def __str__(self):
        return f'Main Course:{self.main_course},Side Dish:{self.side_dish},Drink:{self.drink},Dessert:{self.dessert}'


# Builder
class MenuBuilder(ABC):
    @abstractmethod
    def add_main_course(self, main_course):
        pass

    def add_side_dish(self, side_dish):
        pass

    def add_drink(self, add_drink):
        pass

    def add_dessert(self, add_dessert):
        pass

    def get_menu(self):
        pass


# VegetarianMenuBuilder: Concrete of MenuBuilder
class VegetarianMenuBuilder(MenuBuilder):
    def __init__(self):
        self.menu = Menu()

    def add_main_course(self, main_course):
        self.menu.main_course = main_course

    def add_side_dish(self, side_dish):
        self.menu.side_dish = side_dish

    def add_drink(self, drink):
        self.menu.drink = drink

    def add_dessert(self, dessert):
        self.menu.dessert = dessert

    def get_menu(self):
        return self.menu


# NonVegetarianMenuBuilder: Concrete of MenuBuilder
class NonVegetarianMenuBuilder(MenuBuilder):
    def __init__(self):
        self.menu = Menu()

    def add_main_course(self, main_course):
        self.menu.main_course = main_course

    def add_side_dish(self, side_dish):
        self.menu.side_dish = side_dish

    def add_drink(self, drink):
        self.menu.drink = drink

    def add_dessert(self, dessert):
        self.menu.dessert = dessert

    def get_menu(self):
        return self.menu


# MealDirector
class MealDirector:
    def __init__(self, builder):
        self.builder = builder

    def create_veg_meal(self):
        self.builder.add_main_course('Grilled Tofu')
        self.builder.add_side_dish('Salad')
        self.builder.add_drink('Juice')
        self.builder.add_dessert('Fruit Salad')

    def create_non_veg_meal(self):
        self.builder.add_main_course('Grilled Chicken')
        self.builder.add_side_dish('season salad')
        self.builder.add_drink('Fresh Juice')
        self.builder.add_dessert('Chocolate')


# Usage
VegMenuBuilder = VegetarianMenuBuilder()
director = MealDirector(VegMenuBuilder)
director.create_veg_meal()
VegMenu = VegMenuBuilder.get_menu()
print(VegMenu)

NonVegMenuBuilder = NonVegetarianMenuBuilder()
director = MealDirector(NonVegMenuBuilder)
director.create_non_veg_meal()
NonVegMenu = NonVegMenuBuilder.get_menu()
print(NonVegMenu)