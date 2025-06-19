from src.product import Product

def test_apply_discount():
    p = Product("Item", 100.0, 0)
    p.apply_discount(10)
    assert p.price == 90.0

def test_is_in_stock_true():
    p = Product("Item", 10.0, 5)
    assert p.is_in_stock()

def test_is_in_stock_false():
    p = Product("Item", 10.0, 0)
    assert not p.is_in_stock()