import random

from product import Product
from tax_calculator import TaxCalculator
from tax_rates import TaxRates


class OrderElement:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def __str__(self):
        return f"{self.product} | Quantity {self.quantity:<8}"\
               f" | Tax rate {TaxRates.get_tax_rate(self) * 100:<6.2f}"\
               f"% | Tax value: {TaxCalculator.calculate_tax(self):<8.2f} |"

    def __eq__(self, other: 'OrderElement'):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.product == other.product and self.quantity == other.quantity

    def get_order_element_price(self):
        return self.product.price * self.quantity

    @classmethod
    def generate_random_order_element(cls):
        product = Product.generate_random_product(random.randint(1, 10))
        return OrderElement(product, quantity=random.randint(1, 6))
