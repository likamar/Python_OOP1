from shop.data_generator import generate_random_order, generate_random_order_element
from shop.discount_policy import DiscountPolicy

if __name__ == "__main__":

    # print("Discount policy exercise:")
    # default_order = generate_random_order()
    # loyal_customer_order = generate_random_order(3, discount_policy=DiscountPolicy.loyal_customer)
    # christmas_order = generate_random_order(5, discount_policy=DiscountPolicy.christmas)
    #
    # print("Default order:\n", default_order)
    # print("Loyal customer order:\n", loyal_customer_order)
    # print("Christmas order:\n", christmas_order)

    new_order = generate_random_order(number_of_products=9, discount_policy=DiscountPolicy.loyal_customer)
    print(new_order)
    new_order.add_order_element(generate_random_order_element(10))
    print(new_order)

    # for order_element in new_order.elements:
    #     print(order_element)
