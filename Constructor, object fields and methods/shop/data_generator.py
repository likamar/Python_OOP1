import random

from shop.discount_policy import DiscountPolicy
from shop.order import Order
from shop.order_element import OrderElement
from shop.product import Product


def generate_random_price():
    random_price = random.uniform(1.99, 29.99)
    return round(random_price, 2)


def generate_random_product(product_number: int) -> 'Product':
    random_name = "Product_" + str(product_number)
    random_category = "Category_" + str(product_number)
    random_price = generate_random_price()
    return Product(random_name, random_category, random_price)


def generate_random_order_element():
    product = generate_random_product(random.randint(1, 10))
    return OrderElement(product, quantity=random.randint(1, 6))


def generate_random_order(order_elements_number, discount_policy=None) -> 'Order':
    elements_list: list = []
    for random_int in range(1, order_elements_number + 1):
        order_element = generate_random_order_element()
        elements_list.append(order_element)
    return Order("test_name", "test_surname", elements_list, discount_policy)


def generate_random_orders_sorted_by_price(number_of_orders):
    orders = []
    for _ in range(0, number_of_orders):
        order_elements_number = random.randint(1, 5)
        order = generate_random_order(order_elements_number, discount_policy=DiscountPolicy.christmas)
        orders.append(order)
    orders.sort(key=lambda order_to_sort: order_to_sort.total_price)
    for order in orders:
        print(order)
