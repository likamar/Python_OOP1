from shop.product import Product
from shop.tax_calculator import TaxCalculator
from shop.tax_rates import TaxRates


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
