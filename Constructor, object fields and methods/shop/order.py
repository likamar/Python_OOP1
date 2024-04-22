import random

from shop.order_element import OrderElement
from shop.product import Product


class Order:
    MAX_ELEMENTS = 10

    def __init__(self, customer_name, customer_surname, order_elements: list = None):
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        if order_elements is None:
            self._elements = []
        if len(order_elements) > Order.MAX_ELEMENTS:
            self._elements = order_elements[:20]
        else:
            self._elements = order_elements
        self.total_price = self._calculate_total_price()
        self.elements_number = len(self)

    def __str__(self):
        mark_line = "*" * 20
        client_details = f"Customer: {self.customer_name} {self.customer_surname}"
        elements_number = f"Order items: {self.elements_number}"
        price_details = f"Total price: {self.total_price:.2f}"
        products_details = f"Ordered Products:\n\n "
        for element in self._elements:
            products_details += f"\t{element}\n"
        result = "\n".join([mark_line, client_details, elements_number, price_details, products_details, mark_line])
        return result

    def __len__(self):
        return len(self._elements)

    def __eq__(self, other: 'Order'):
        if self.__class__ != other.__class__:
            return NotImplemented

        if self.elements_number != other.elements_number:
            return False

        if self.customer_name != other.customer_name or self.customer_surname != other.customer_surname:
            return False

        for order_element in self._elements:
            if order_element not in other._elements:
                return False

        return True

    # def print_details(self):
    #     print("Order details:\n")
    #     print("Name: ", self.customer_name)
    #     print("Surname: ", self.customer_surname)
    #     print("Products:")
    #     for element in self.elements:
    #         element.print_order_element()
    #     print(f"Total price: {self.total_price:.2f}")
    #     print("#" * 20)

    def add_order_element(self, order_element: OrderElement):
        self._elements.append(order_element)

    def _calculate_total_price(self) -> float:
        total_price = 0
        for order_element in self._elements:
            total_price += order_element.get_order_element_price()
        return total_price

    def add_product(self, product: Product, quantity: int):
        if self.elements_number < Order.MAX_ELEMENTS:
            new_element = OrderElement(product, quantity)
            self._elements.append(new_element)
            self.total_price = self._calculate_total_price()
            self.elements_number = len(self)
        else:
            print("Maximum products limit reached!")

    @classmethod
    def generate_random_order(cls) -> 'Order':
        elements_list: list = []
        for random_int in range(1, random.randint(2, cls.MAX_ELEMENTS)):
            order_element = OrderElement.generate_random_order_element()
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
