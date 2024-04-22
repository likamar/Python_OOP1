class TaxRates:
    FRUITS = 0.05
    FOOD = 0.08
    OTHER = 0.20

    @staticmethod
    def get_tax_rate(order_element):
        product_category = order_element.product.category
        if product_category == "fruits":
            tax_rate = TaxRates.FRUITS
        elif product_category == "food":
            tax_rate = TaxRates.FOOD
        else:
            tax_rate = TaxRates.OTHER
        return tax_rate
