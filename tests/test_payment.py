import pytest
from src.payment import Payment

class DummyPM:
    def __init__(self):
        self.charged = 0
    def charge(self, amount):
        self.charged = amount
        return True

def test_process_payment():
    pm = DummyPM()
    payment = Payment(123.45)
    assert payment.process(pm) is True
    assert pm.charged == 123.45

@pytest.mark.parametrize("card,valid", [
    ("1234567812345678", True),
    ("abcd", False),
    (1234567812345678, False),
])
def test_validate_card(card, valid):
    payment = Payment(0)
    assert payment.validate_card(card) is valid