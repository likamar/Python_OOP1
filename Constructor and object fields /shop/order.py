import random

from shop.product import generate_random_product


class Order:
    def __init__(self, customer_name, customer_surname, products: list = None):
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        if products is None:
            self.products = []
        self.products = products
        self.total_price = get_total_price(products)

    def print_details(self):
        print("Order details:\n")
        print("Name: ", self.customer_name)
        print("Surname: ", self.customer_surname)
        print("Products:")
        for product in self.products:
            product.print_details()
        print(f"Total price: {self.total_price:.2f}")
        print("#" * 20)


def get_total_price(products: list):
    total_price = 0
    for product in products:
        total_price += product.price
    return total_price


def generate_random_order():
    products_list = []
    for product_number in range(1, random.randint(2, 10)):
        print("Product number: ", product_number)
        product = generate_random_product(product_number)
        products_list.append(product)
    return Order("user_name", "user_surname", products_list)
