import random

from shop.Product import print_product_details, generate_random_product


class Order:
    def __init__(self, customer_name, customer_surname, products: list = None):
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        if products is None:
            self.products = []
        self.products = products
        self.total_price = get_total_price(products)


def get_total_price(products: list):
    total_price = 0
    for product in products:
        total_price += product.price
    return total_price


def print_order_details(order: Order):
    print("Order details:\n")
    print("Name: ", order.customer_name)
    print("Surname: ", order.customer_surname)
    print("Products:")
    for product in order.products:
        print_product_details(product)
    print(f"Total price: {order.total_price:.2f}")
    print("###################")


def generate_random_order():
    products_list = []
    for product_number in range(1, random.randint(1, 10)):
        product = generate_random_product(product_number)
        products_list.append(product)
    return Order("user_name", "user_surname", products_list)