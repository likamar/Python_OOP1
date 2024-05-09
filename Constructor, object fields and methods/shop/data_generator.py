import random

from shop.discount_policy import DiscountPolicy
from shop.order import Order
from shop.order_element import OrderElement
from shop.product import Product

MIN_ORDER_ELEMENT_QUANTITY = 1
MAX_ORDER_ELEMENT_QUANTITY = 10
MIN_PRODUCT_PRICE = 0.99
MAX_PRODUCT_PRICE = 99.99
MIN_IDENTIFIER = 1
MAX_IDENTIFIER = 9999


def generate_random_price():
    random_price = random.uniform(MIN_PRODUCT_PRICE, MAX_PRODUCT_PRICE)
    return round(random_price, 2)


def generate_random_product(product_number: int) -> 'Product':
    random_name = "Product_" + str(product_number)
    random_id = random.randint(MIN_IDENTIFIER, MAX_IDENTIFIER)
    random_category = "Category_" + str(product_number)
    random_price = generate_random_price()
    return Product(random_name, random_id, random_category, random_price)


def generate_random_order_element(element_number):
    quantity = random.randint(MIN_ORDER_ELEMENT_QUANTITY, MAX_ORDER_ELEMENT_QUANTITY)
    product = generate_random_product(element_number)
    return OrderElement(product, quantity)


def generate_order_elements(number_of_products=None):
    order_elements = []
    if number_of_products is None:
        number_of_products = random.randint(1, Order.MAX_ELEMENTS)
    for element_number in range(1, number_of_products + 1):
        order_elements.append(generate_random_order_element(element_number))
    return order_elements


def generate_random_order(number_of_products=None, discount_policy=None) -> 'Order':
    elements_list = generate_order_elements(number_of_products)
    return Order("test_name", "test_surname", elements_list, discount_policy)


def generate_random_orders_sorted_by_price(number_of_orders):
    orders = []
    for _ in range(0, number_of_orders):
        order_elements_number = random.randint(MIN_ORDER_ELEMENT_QUANTITY, MAX_ORDER_ELEMENT_QUANTITY)
        order = generate_random_order(order_elements_number)
        orders.append(order)
    orders.sort(key=lambda order_to_sort: order_to_sort.total_price)
    for order in orders:
        print(order)
