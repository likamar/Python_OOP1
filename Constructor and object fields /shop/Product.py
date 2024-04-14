import random


class Product:
    def __init__(self, name, category=None, price: float = 0):
        self.name = name
        self.category = category
        self.price = price


def print_product_details(product: Product):
    print()
    print("\tProduct name: ", product.name)
    print("\tCategory: ", product.category)
    print(f"\tPrice: {product.price:.2f}")
    print()


def generate_random_product(product_number: int):
    random_name = "Product_" + str(product_number)
    random_category = "Category_" + str(product_number)
    random_price = generate_random_price()
    return Product(random_name, random_category, random_price)


def generate_random_price():
    return random.uniform(1.99, 29.99)
