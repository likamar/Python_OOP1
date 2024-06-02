from shop.data_generator import generate_random_order, generate_random_order_element, generate_random_product
from shop.data_generator import generate_order_elements
from shop.discount_policy import DiscountPolicy
from shop.percentage_discount import PercentageDiscount
from shop.absolute_discount import AbsoluteDiscount
from shop.expiring_product import ExpiringProduct
from shop.express_order import ExpressOrder
from shop.order import Order
from shop.product import Product
from shop.order_element import OrderElement
import random

if __name__ == "__main__":

    print("Discount policy exercise:")
    default_order = generate_random_order()
    loyal_customer_order = generate_random_order(3, discount_policy=PercentageDiscount(10))
    christmas_order = generate_random_order(5, discount_policy=AbsoluteDiscount(50))

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

    product = Product(name="Samsung TV", identifier=99, category="Electronics", price=2999.99)
    order_element = OrderElement(product, quantity=1)
    order_elements = [order_element]
    express_order = ExpressOrder(customer_name="Marcin", customer_surname="Lika", order_elements=order_elements, delivery_date="2024-05-06", discount_policy=PercentageDiscount(10))
    print(express_order)

    order_1 = generate_random_order(number_of_products=4)
    order_2 = generate_random_order(number_of_products=4)

    print(order_1)
    print(order_2)
    print(order_1 == order_2)

    order_2.add_product(generate_random_product(1), 2)
    order_2.add_product(generate_random_product(1), 2)
    order_2.add_product(generate_random_product(1), 2)
    order_2.add_product(generate_random_product(1), 2)
    order_2.add_product(generate_random_product(1), 2)
    order_2.add_product(generate_random_product(1), 2)
    order_2.add_product(generate_random_product(1), 2)

    print(order_1)
    print(order_2)

    # print("List comprehension/ex_1")
    # # Zadanie 1
    # # Użyj dict comprehensions, aby zamienić listę pozycji zamówienia w słownik, gdzie kluczem będzie
    # # identyfikator produktu z danej pozycji, a wartością będzie dany obiekt klasy Product.
    #
    # order_elements = generate_order_elements(number_of_products=10)
    # order_elems_dict = {order_element.product.identifier: order_element.product for order_element in order_elements}
    # print(type(order_elems_dict))
    # print(order_elems_dict)
    #
    # print("List comprehension/ex_2")
    # # Zmodyfikuj rozwiązanie poprzedniego zadania.
    #
    # # Skorzystaj z dict comprehensions, aby na podstawie słownika z produktami stworzyć nowy,
    # # w którym każdy produkt będzie pod kluczem o 1 większym.
    # # I tak produkt, który znajdował się w oryginalnym słowniku pod kluczem 15 trafi w nowym pod klucz 16, itd.
    # # Następnie skorzystaj z metody update aby “połączyć” oba słowniki.
    #
    # incremented_order_elems_dict = {identifier + 1: product for identifier, product in order_elems_dict.items()}
    # print(type(incremented_order_elems_dict))
    # print(incremented_order_elems_dict)
    #
    # order_elems_dict.update(incremented_order_elems_dict)
    # print(order_elems_dict)

    def products_delivery():
        available_products = [
            "bread",
            "buns",
            "milk",
            "eggs",
            "butter",
            "cheese",
            "ham",
            "sausages",
            "chocolate",
            "water"
        ]
        return [available_products[random.randint(0, 9)] for _ in range(5)]


    needed_products = [
        "bread",
        "buns",
        "milk",
        "eggs",
        "butter",
        "cheese",
        "ham",
        "sausages",
        "chocolate",
        "water"
    ]

    received_products = []

    while not set(needed_products) == set(received_products):
        new_products = products_delivery()
        received_products += new_products
        print(f"Received products: {received_products}")
        missing_products = set(needed_products).difference(set(received_products))
        print(f"Waiting for delivery: {missing_products}")

