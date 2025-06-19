class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def apply_discount(self, percent):
        self.price *= (1 - percent / 100)

    def is_in_stock(self):
        return self.stock > 0