from src.product import Product
from src.inventory import Inventory
from src.order import Order
from src.payment import Payment

class DummyPM:
    def __init__(self):
        self.charged = 0.0
    def charge(self, amount):
        self.charged = amount
        return True

def test_order_inventory_payment_integration():
    # 1) Crio produto e estoque
    prod = Product("Burger", 10.0, 5)
    inv = Inventory()git
    inv.add_product(prod, 5)
    assert inv.products[prod] == 5

    # 2) Faço pedido de 2 unidades
    order = Order()
    order.add_item(prod, 2)
    assert (prod, 2) in order.items

    # 3) Atualizo o estoque
    inv.remove_product(prod, 2)
    assert inv.products[prod] == 3

    # 4) Processamento de pagamento pela integração Payment
    payment = Payment(10.0 * 2)
    pm = DummyPM()
    assert payment.process(pm)
    assert pm.charged == 20.0
