import random


class Product:
    def __init__(self, name, category=None, price: float = 0):
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f"| Product: {self.name:<10} | Category: {self.category:<12} | Unit price: {self.price:<8.2f}"

    def __eq__(self, other: 'Product'):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (self.name == other.name and
                self.category == other.category and
                self.price == other.price)

    @classmethod
    def generate_random_product(cls, product_number: int) -> 'Product':
        random_name = "Product_" + str(product_number)
        random_category = "Category_" + str(product_number)
        random_price = generate_random_price()
        return Product(random_name, random_category, random_price)

    # def print_details(self):
    #     # print()
    #     print("\tProduct name: ", self.name)
    #     print("\tCategory: ", self.category)
    #     print(f"\tUnit price: {self.price:.2f}")
    #     # print()


def generate_random_price():
    random_price = random.uniform(1.99, 29.99)
    return round(random_price, 2)


# test_product = Product(name="test_product", category="test_category", price=10)
# print(test_product)
