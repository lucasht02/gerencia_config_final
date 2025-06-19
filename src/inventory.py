class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        self.products[product] = self.products.get(product, 0) + quantity

    def remove_product(self, product, quantity):
        if product in self.products and self.products[product] >= quantity:
            self.products[product] -= quantity