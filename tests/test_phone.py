import pytest
from src.phone import Phone
from src.item import Item

@pytest.fixture
def phone1():
    return Phone("Смартфон", 10000, 20, 2)

def test_set_sim(phone1):
    assert phone1.number_of_sim == 2
    phone1.number_of_sim = 1
    assert phone1.number_of_sim == 1

def test_add(phone1):
    phone2 = Item("Смартфон", 10000, 10)
    assert phone2 + phone1 == 30
    assert phone1 + phone1 == 40

def test_dundr_methods(phone1):
    assert repr(phone1) == "Phone('Смартфон', 10000, 20, 2)"
    assert str(phone1) == 'Смартфон'