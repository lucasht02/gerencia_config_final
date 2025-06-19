from src.flow import run_order_flow

def test_end_to_end_order_flow():
    resultado = run_order_flow("cliente1", "Pizza", 25.0, 10, 3)

    # A função retorna apenas a linha de assunto, conforme implementação de send_email()
    esperado = "Email sent to cliente1@exemplo.com with subject 'Pedido Confirmado'"
    assert resultado == esperado
