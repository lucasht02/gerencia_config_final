import pytest
from src.user import User

def test_authenticate_success():
    u = User("alice", "senha123")
    assert u.authenticate("senha123")

def test_authenticate_fail():
    u = User("alice", "senha123")
    assert not u.authenticate("outrasenha")

def test_update_profile():
    u = User("bob", "abc")
    u.update_profile(new_username="robert", new_password="xyz")
    assert u.username == "robert"
    assert u.password == "xyz"