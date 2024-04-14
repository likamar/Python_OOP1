from shop.Order import Order, print_order_details, generate_random_order
from shop.Product import Product

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

    print_order_details(order_1)
    print_order_details(order_2)
    print_order_details(order_3)

    print_order_details(generate_random_order())
