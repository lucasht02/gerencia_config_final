from src.user import User
from src.product import Product
from src.inventory import Inventory
from src.order import Order
from src.payment import Payment
from src.notification import Notification

class DummyPaymentMethod:
    def __init__(self):
        self.charged = 0.0
    def charge(self, amount):
        self.charged = amount
        return True

def run_order_flow(username: str, product_name: str, price: float, initial_stock: int, quantity: int) -> str:
    # 1. Criar usuário
    user = User(username, "senhaTeste")
    assert user.authenticate("senhaTeste")

    # 2. Cadastrar produto e estoque
    prod = Product(product_name, price, initial_stock)
    inv = Inventory()
    inv.add_product(prod, initial_stock)
    assert prod.is_in_stock()

    # 3. Fazer pedido
    order = Order()
    order.add_item(prod, quantity)

    # 4. Atualizar estoque
    inv.remove_product(prod, quantity)
    assert inv.products[prod] == initial_stock - quantity

    # 5. Processar pagamento
    pm = DummyPaymentMethod()
    payment = Payment(price * quantity)
    assert payment.process(pm)
    assert pm.charged == price * quantity

    # 6. Enviar notificação
    notif = Notification(f"{username}@exemplo.com")
    msg = notif.send_email("Pedido Confirmado",
                           f"Usuário {username}, seu pedido de {quantity}x {product_name} foi confirmado.")
    return msg
