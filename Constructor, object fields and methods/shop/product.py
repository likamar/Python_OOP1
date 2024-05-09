class Product:
    def __init__(self, name, identifier, category='None', price: float = 0):
        self.name = name
        self.identifier = identifier
        self.category = category
        self.price = price

    def __str__(self):
        return f"ID: {self.identifier} | Product: {self.name:<10} | Category: {self.category:<12} | " \
               f"Unit price: {self.price:<8.2f}"

    def __eq__(self, other: 'Product'):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (self.name == other.name and
                self.category == other.category and
                self.price == other.price)

    @staticmethod
    def format_product_id(identifier):
        return str(identifier).zfill(5)
