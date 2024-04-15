class Apple:
    def __init__(self, species, size, price_kg):
        self.size = size
        self.species = species
        self.price_kg = price_kg

    def get_total_price(self, quantity_kg):
        return self.price_kg * quantity_kg
