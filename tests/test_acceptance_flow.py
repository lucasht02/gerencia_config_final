from src.flow import run_order_flow

def test_end_to_end_order_flow():
    resultado = run_order_flow("cliente1", "Pizza", 25.0, 10, 3)

    assert "cliente1" in resultado
    assert "3x Pizza" in resultado
    assert "Confirmado" in resultado
