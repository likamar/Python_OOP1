class Product:
    pass


class Order:
    pass


class Apple:
    pass


class Potato:
    pass


if __name__ == "__main__":
    apple_1 = Apple()
    apple_2 = Apple()
    apple_3 = Apple()

    potato_1 = Potato()
    potato_2 = Potato()
    potato_3 = Potato()

    print("apple_1 type: ", type(apple_1))
    print("apple_2 type: ", type(apple_2))
    print("apple_3 type: ", type(apple_3))

    print("potato_1 type: ", type(potato_1))
    print("potato_2 type: ", type(potato_2))
    print("potato_3 type: ", type(potato_3))

    orders = []

    for order in range(5):
        orders.append(Order())

    products = {
        "product_1": Product(),
        "product_2": Product(),
        "product_3": Product(),
        "product_4": Product(),
        "product_5": Product(),
    }

    for (index, order) in enumerate(orders):
        print(f"{index}: {order}")

    for (product_name, product_object) in products.items():
        print(f"{product_name}: {product_object}")
