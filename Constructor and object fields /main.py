from shop.order import Order, generate_random_order
from shop.product import Product
from shop.apple import Apple
from shop.potato import Potato

if __name__ == "__main__":
    bread = Product(name="bread", category="food", price=4)
    water = Product(name="water", category="drinks", price=3.5)
    shampoo = Product(name="shampoo", category="cosmetics", price=19.99)
    ham = Product(name="ham", category="food", price=6.99)

    products_list_1 = [bread, water, shampoo, ham]
    products_list_2 = [bread, ham]
    products_list_3 = [bread, ham, water]

    order_1 = Order(customer_name="Jan", customer_surname="Kowalski", products=products_list_1)
    order_2 = Order(customer_name="Adam", customer_surname="Nowak", products=products_list_2)
    order_3 = Order(customer_name="Dorota", customer_surname="Gajewska", products=products_list_3)

    order_1.print_details()
    order_2.print_details()
    order_3.print_details()

    random_order = generate_random_order()
    random_order.print_details()

    test_apple = Apple(species="Jonagold", size="L", price_kg=3.99)
    test_potato = Potato(species="Bryza", size="M", price_kg=1.99)

    print(f"Total price for 5 kq of apples: {test_apple.get_total_price(5):.2f}")
    print(f"Total price for 10 kq of potatoes: {test_potato.get_total_price(10):.2f}")
