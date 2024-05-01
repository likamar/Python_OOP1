class Product:
    def __init__(self, name, category='None', price: float = 0):
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f"| Product: {self.name:<10} | Category: {self.category:<12} | Unit price: {self.price:<8.2f}"

    def __eq__(self, other: 'Product'):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (self.name == other.name and
                self.category == other.category and
                self.price == other.price)
