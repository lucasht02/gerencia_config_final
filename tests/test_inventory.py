from src.inventory import Inventory
from src.product import Product

def test_add_product():
    inv = Inventory()
    prod = Product("Y", 20.0, 5)
    inv.add_product(prod, 3)
    assert inv.products[prod] == 3

def test_remove_product_success():
    inv = Inventory()
    prod = Product("Y", 20.0, 5)
    inv.add_product(prod, 5)
    inv.remove_product(prod, 2)
    assert inv.products[prod] == 3

def test_remove_product_insufficient():
    inv = Inventory()
    prod = Product("Y", 20.0, 5)
    inv.add_product(prod, 1)
    inv.remove_product(prod, 2)
    assert inv.products[prod] == 1