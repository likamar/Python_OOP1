from shop.data_generator import generate_random_order, generate_random_order_element
from shop.discount_policy import DiscountPolicy
from shop.expiring_product import ExpiringProduct
from shop.express_order import ExpressOrder
from shop.product import Product
from shop.order_element import OrderElement

if __name__ == "__main__":

    print("Discount policy exercise:")
    default_order = generate_random_order()
    loyal_customer_order = generate_random_order(3, discount_policy=DiscountPolicy.loyal_customer)
    christmas_order = generate_random_order(5, discount_policy=DiscountPolicy.christmas)

    print("Default order:\n", default_order)
    print("Loyal customer order:\n", loyal_customer_order)
    print("Christmas order:\n", christmas_order)

    # new_order = generate_random_order(number_of_products=9, discount_policy=DiscountPolicy.loyal_customer)
    # print(new_order)
    # new_order.add_order_element(generate_random_order_element(10))
    # print(new_order)
    #
    # my_product = ExpiringProduct(name="Pepsi", production_year=2022, years_to_expire=3)
    # print(my_product)
    # print(my_product.does_expire(current_year=2024))

    product = Product(name="Samsung TV", category="Electronics", price=2999.99)
    order_element = OrderElement(product, quantity=1)
    order_elements = [order_element]
    express_order = ExpressOrder(customer_name="Marcin", customer_surname="Lika", order_elements=order_elements, delivery_date="2024-05-06",discount_policy=DiscountPolicy.christmas)
    print(express_order)
