import pytest
from src.validator import Validator

@pytest.fixture
def validator():
    return Validator()

def test_is_email_valid_true(validator):
    assert validator.is_email_valid("usuario@exemplo.com")

@pytest.mark.parametrize("email", [
    "invalido", "teste@.com", "abc@dominio", "nome@dominio,com"
])
def test_is_email_valid_false(validator, email):
    assert not validator.is_email_valid(email)

def test_is_password_strong_true(validator):
    assert validator.is_password_strong("SenhaForte1")

@pytest.mark.parametrize("pwd", [
    "curta1A",       # menos de 8 caracteres
    "semNumeroA",    # sem dígito
    "semmaiuscula1", # sem maiúscula
])
def test_is_password_strong_false(validator, pwd):
    assert not validator.is_password_strong(pwd)
