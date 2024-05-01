from shop.product import Product


class ExpiringProduct(Product):
    def __init__(self, name, production_year, years_to_expire, category='None', price: float = 0):
        super().__init__(name, category, price)
        self.production_year = production_year
        self.years_to_expire = years_to_expire

    def does_expire(self, current_year: int) -> bool:
        return current_year > self.production_year + self.years_to_expire
