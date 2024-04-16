import random


class Product:
    def __init__(self, name, category=None, price: float = 0):
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f"| Product: {self.name:<15} | Category: {self.category:<15} | Unit price: {self.price:<10.2f}"

    # def print_details(self):
    #     # print()
    #     print("\tProduct name: ", self.name)
    #     print("\tCategory: ", self.category)
    #     print(f"\tUnit price: {self.price:.2f}")
    #     # print()


def generate_random_product(product_number: int):
    random_name = "Product_" + str(product_number)
    random_category = "Category_" + str(product_number)
    random_price = generate_random_price()
    return Product(random_name, random_category, random_price)


def generate_random_price():
    random_price = random.uniform(1.99, 29.99)
    return round(random_price, 2)


# test_product = Product(name="test_product", category="test_category", price=10)
# print(test_product)