from shop.apple import Apple
from shop.order import Order, generate_random_order
from shop.order_element import OrderElement
from shop.potato import Potato
from shop.product import Product

if __name__ == "__main__":
    bread = Product(name="bread", category="food", price=4)
    water = Product(name="water", category="drinks", price=3.5)
    shampoo = Product(name="shampoo", category="cosmetics", price=19.99)
    ham = Product(name="ham", category="food", price=6.99)

    order_element_1 = OrderElement(bread, quantity=4)
    order_element_2 = OrderElement(water, 12)
    order_element_3 = OrderElement(shampoo, 3)
    order_element_4 = OrderElement(ham, 2)
    order_element_5 = OrderElement(bread, quantity=1)

    order_list_1 = [order_element_1, order_element_2, order_element_3]
    order_list_2 = [order_element_2, order_element_3, order_element_4]
    order_list_3 = [order_element_4, order_element_2, order_element_1]
    order_list_4 = [order_element_1, order_element_2, order_element_3]
    order_list_5 = [order_element_1, order_element_2, order_element_3, order_element_4]
    order_list_6 = [order_element_1, order_element_2, order_element_3, order_element_5]
    order_list_7 = [order_element_2, order_element_3, order_element_1]

    order_1 = Order(customer_name="Jan", customer_surname="Kowalski", order_elements=order_list_1)
    order_2 = Order(customer_name="Adam", customer_surname="Nowak", order_elements=order_list_2)
    order_3 = Order(customer_name="Dorota", customer_surname="Gajewska", order_elements=order_list_3)
    order_4 = Order(customer_name="Jan", customer_surname="Kowalski", order_elements=order_list_4)
    order_5 = Order(customer_name="Jan", customer_surname="Nowak", order_elements=order_list_4)
    order_6 = Order(customer_name="Jan", customer_surname="Nowak", order_elements=order_list_5)
    order_7 = Order(customer_name="Jan", customer_surname="Nowak", order_elements=order_list_6)
    order_8 = Order(customer_name="Jan", customer_surname="Kowalski", order_elements=order_list_7)

    print(order_1)
    print(order_2)
    print(order_3)

    random_order = generate_random_order()
    print(random_order)

    test_apple = Apple(species="Jonagold", size="L", price_kg=3.99)
    test_potato = Potato(species="Bryza", size="M", price_kg=1.99)

    print(f"{test_apple} {'|':>5} Total price for 5 kg: {test_apple.get_total_price(5):.2f}")
    print(f"{test_potato} {'|':>5} Total price for 10 kg: {test_potato.get_total_price(10):.2f}")
    print()

    cheese_1 = Product(name="cheese", category="food", price=49.99)
    cheese_2 = Product(name="cheese", category="food", price=49.99)
    cheese_3 = Product(name="cheese", category="food", price=59.99)

    print(f"cheese_1 = cheese_2: {cheese_1 == cheese_2}")
    print(f"cheese_1 = cheese_3: {cheese_1 == cheese_3}")
    print(f"cheese_2 = cheese_3: {cheese_2 == cheese_3}")
    print()

    order_element_1 = OrderElement(product=cheese_1, quantity=1)
    order_element_2 = OrderElement(product=cheese_2, quantity=1)
    order_element_3 = OrderElement(product=cheese_2, quantity=2)
    order_element_4 = OrderElement(product=cheese_3, quantity=2)

    print(f"order_element_1 = order_element_2: {order_element_1 == order_element_2}")
    print(f"order_element_1 = order_element_3: {order_element_1 == order_element_3}")
    print(f"order_element_1 = order_element_4: {order_element_1 == order_element_4}")
    print(f"order_element_2 = order_element_3: {order_element_2 == order_element_3}")
    print(f"order_element_2 = order_element_4: {order_element_2 == order_element_4}")
    print(f"order_element_3 = order_element_4: {order_element_3 == order_element_4}")
    print()

    print(f"order_1 = order_2: {order_1 == order_2}")  # False
    print(f"order_1 = order_4: {order_1 == order_4}")  # True
    print(f"order_4 = order_5: {order_4 == order_5}")  # False
    print(f"order_6 = order_5: {order_6 == order_5}")  # False
    print(f"order_6 = order_7: {order_6 == order_7}")  # False
    print(f"order_1 = order_8: {order_1 == order_8}")  # True

    print(type(bread == 1))
    print(type(NotImplemented))
