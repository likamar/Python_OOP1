import random

from shop.order import Order
from shop.discount_policy import DiscountPolicy


def get_order_price(order: Order):
    return order.total_price





if __name__ == "__main__":
    print("Random orders sorted by price:")
    generate_random_orders_sorted_by_price(5)

    print("Discount policy exercise:")
    default_order = Order.generate_random_order(4)
    loyal_customer_order = Order.generate_random_order(4, discount_policy=DiscountPolicy.loyal_customer)
    christmas_order = Order.generate_random_order(4, discount_policy=DiscountPolicy.christmas)

    print("Default order:\n", default_order)
    print("Loyal customer order:\n", loyal_customer_order)
    print("Christmas order:\n", christmas_order)
