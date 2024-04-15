from product import Product


class OrderElement:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def print_order_element(self):
        self.product.print_details()
        print(f"\tQuantity: {self.quantity}")
        print(f"\tPrice: {self.get_order_element_price():.2f}")

    def get_order_element_price(self):
        return self.product.price * self.quantity


# test_product = Product(name="test_product", category="test_category", price=10)
# test_order_element = OrderElement(test_product, 5)
# test_order_element.print_order_element()
