from shop.discount_policy import DiscountPolicy


class PercentageDiscount(DiscountPolicy):
    def __init__(self, discount_percentage):
        self.discount_percentage = discount_percentage

    def apply_discount(self, total_price):
        return total_price * (1 - self.discount_percentage / 100)
