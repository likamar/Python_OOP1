class Potato:
    def __init__(self, species, size, price_kg):
        self.size = size
        self.species = species
        self.price_kg = price_kg

    def __repr__(self):
        return f"Potato | Species: {self.species:<10} | Size: {self.size:<5} | Price: {self.price_kg:.2f} / kg"

    def get_total_price(self, quantity_kg):
        return self.price_kg * quantity_kg
