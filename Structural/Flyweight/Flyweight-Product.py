# Intrinsic State
class ProductType:
    def __init__(self, category, brand):
        self.category = category
        self.brand = brand

    def display(self, name, price):
        print(f'Product: {name},Category:{self.category},Brand:{self.brand},Price:{price}')


# Flyweight Factory
class ProductFactory:

    _product_types = {}

    @classmethod
    def get_product_type(cls, category, brand):
        key = (category, brand)
        if key not in cls._product_types:
            cls._product_types[key] = ProductType(category, brand)
        return cls._product_types[key]


# The Product class represents the context, which includes the extrinsic state (e.g., name, price).
class Product:
    def __init__(self, name, price, product_type):
        self.name = name
        self.price = price
        self.product_type = product_type

    def display(self):
        self.product_type.display(self.name, self.price)


# Using the Flyweight
class ECommerceSite:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, category, brand):
        product_type = ProductFactory.get_product_type(category, brand)

        product = Product(name, price, product_type)
        self.products.append(product)

    def display_products(self):
        for product in self.products:
            product.display()


# Usage
ecommerce = ECommerceSite()
ecommerce.add_product('Car', '2000', 'Vehicle', 'Toyota')
ecommerce.add_product("MacBook Pro", 1299, "Electronics", "Apple")
ecommerce.add_product("Dell XPS 13", 999, "Electronics", "Dell")
ecommerce.add_product("iPad Pro", 799, "Electronics", "Apple")

ecommerce.display_products()