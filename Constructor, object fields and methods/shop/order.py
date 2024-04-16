import random

from shop.order_element import OrderElement, generate_random_order_element
from shop.product import Product
from shop.product import generate_random_product


class Order:
    def __init__(self, customer_name, customer_surname, order_elements: list = None):
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        if order_elements is None:
            self.elements = []
        self.elements = order_elements
        self.total_price = self.get_total_price()

    def print_details(self):
        print("Order details:\n")
        print("Name: ", self.customer_name)
        print("Surname: ", self.customer_surname)
        print("Products:")
        for element in self.elements:
            element.print_order_element()
        print(f"Total price: {self.total_price:.2f}")
        print("#" * 20)

    def add_order_element(self, order_element: OrderElement):
        self.elements.append(order_element)

    def get_total_price(self) -> float:
        total_price = 0
        for order_element in self.elements:
            total_price += order_element.get_order_element_price()
        return total_price


def generate_random_order() -> Order:
    elements_list: list = []
    for random_int in range(1, random.randint(2, 6)):
        order_element = generate_random_order_element()
        elements_list.append(order_element)
    return Order("test_name", "test_surname", elements_list)


# test_product = Product(name="test_product", category="test_category", price=10)
# order_elements = []
# order_element_1 = OrderElement(test_product, 5)
# order_element_2 = OrderElement(test_product, 2)
# order_elements.append(order_element_1)
# order_elements.append(order_element_2)
# test_order = Order(customer_name="Jan", customer_surname="Kowalski", order_elements=order_elements)
# test_order.print_details()
