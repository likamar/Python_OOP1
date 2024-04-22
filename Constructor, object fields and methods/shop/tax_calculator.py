from shop.tax_rates import TaxRates


class TaxCalculator:
    @staticmethod
    def calculate_tax(order_element):
        order_element_price = order_element.product.price * order_element.quantity
        return order_element_price * TaxRates.get_tax_rate(order_element)
