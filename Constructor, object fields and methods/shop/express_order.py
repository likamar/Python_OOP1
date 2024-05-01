from shop.order import Order


class ExpressOrder(Order):
    EXPRESS_DELIVERY_FEE = 29.99

    def __init__(self, delivery_date: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.delivery_date = delivery_date

    def __str__(self):
        delivery_date = f"Delivery date: {self.delivery_date}"
        express_delivery_fee = f"Express delivery fee: {ExpressOrder.EXPRESS_DELIVERY_FEE}"
        result = "\n".join([delivery_date,
                            express_delivery_fee,
                            super().__str__()
                            ])
        return result

    @property
    def total_price(self) -> float:
        return super().total_price + ExpressOrder.EXPRESS_DELIVERY_FEE
