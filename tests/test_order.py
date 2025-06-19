from src.order import Order
from src.product import Product

def test_add_and_remove_item():
    o = Order()
    prod = Product("X", 50.0, 10)
    o.add_item(prod, 2)
    assert (prod, 2) in o.items
    o.remove_item(prod)
    assert all(item[0] != prod for item in o.items)