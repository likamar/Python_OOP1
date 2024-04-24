class DiscountPolicy:

    LOYAL_CUSTOMER_DISCOUNT = 0.05
    CHRISTMAS_DISCOUNT = 20

    @classmethod
    def default(cls, total_price):
        return total_price

    @classmethod
    def loyal_customer(cls, total_price):
        return total_price * (1 - cls.LOYAL_CUSTOMER_DISCOUNT)

    @classmethod
    def christmas(cls, total_price):
        if total_price > 100:
            return total_price - cls.CHRISTMAS_DISCOUNT
        return total_price
