import random

from shop.product import Product, generate_random_product


class OrderElement:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def __str__(self):
        return f"{self.product} | Quantity {self.quantity}"

    def __eq__(self, other: 'OrderElement'):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.product == other.product and self.quantity == other.quantity

    # def print_order_element(self):
    #     self.product.print_details()
    #     print(f"\tQuantity: {self.quantity}")
    #     print(f"\tPrice: {self.get_order_element_price():.2f}")
    #     print("*" * 20)

    def get_order_element_price(self):
        return self.product.price * self.quantity


def generate_random_order_element():
    product = generate_random_product(random.randint(1, 10))
    return OrderElement(product, quantity=random.randint(1, 6))


# test_product = Product(name="test_product", category="test_category", price=10)
# test_order_element = OrderElement(test_product, 5)
# test_order_element.print_order_element()


# random_order_element = generate_random_order_element()
# random_order_element.print_order_element()
