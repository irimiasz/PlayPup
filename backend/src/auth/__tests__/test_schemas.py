import pytest

from src.auth.constants import (
    MESSAGE_PASSWORD_TOO_WEAK,
    MESSAGE_USERNAME_STARTS_WITH_NUMBER,
    MESSAGE_USERNAME_TOO_SHORT,
)
from src.auth.schemas import UserCreate


def test_minimum_username_length():
    with pytest.raises(ValueError) as e:
        UserCreate(email="radek@gmail.com", password="SilneHaslo1!", username="test")
    assert MESSAGE_USERNAME_TOO_SHORT in str(e.value)


def test_username_starts_with_number():
    with pytest.raises(ValueError) as e:
        UserCreate(email="radek@gmail.com", password="SilneHaslo1!", username="11Radek")
    assert MESSAGE_USERNAME_STARTS_WITH_NUMBER in str(e.value)


def test_weak_password_throws_exception():
    with pytest.raises(ValueError) as e:
        UserCreate(email="radek@gmail.com", password="haslo1!!", username="testoviron")
    assert MESSAGE_PASSWORD_TOO_WEAK in str(e.value)


def test_no_exception_thrown_in_user_validation():
    UserCreate(email="radek@gmail.com", password="Haslo1!!", username="testoviron")