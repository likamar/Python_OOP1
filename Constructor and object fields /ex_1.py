class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price


class Order:
    def __init__(self, customer_name, customer_surname, products: list = None):
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        if products is None:
            self.products = []
        self.products = products
        self.total_price = get_total_price(products)


class Apple:
    def __init__(self, species, size, price_kg):
        self.size = size
        self.species = species
        self.price_kg = price_kg


class Potato:
    def __init__(self, species, size, price_kg):
        self.size = size
        self.species = species
        self.price_kg = price_kg


def get_total_price(products: list):
    total_price = 0
    for product in products:
        total_price += product.price
    return total_price


def print_product_details(product: Product):
    print()
    print("\tProduct name: ", product.name)
    print("\tCategory: ", product.category)
    print(f"\tPrice: {product.price:.2f}")
    print()


def print_order_details(order: Order):
    print("Order details:\n")
    print("Name: ", order.customer_name)
    print("Surname: ", order.customer_surname)
    print("Products:")
    for product in order.products:
        print_product_details(product)
    print("Total price: ", order.total_price)
    print("###################")


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
