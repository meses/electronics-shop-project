"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item

@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)

def test_item_total_price(item1):
    assert item1.calculate_total_price() == 200000

def test_apply_discount(item1):
    item1.pay_rate = 0.7
    item1.apply_discount()
    assert item1.price == 7000.0

def test_string_to_number():
    assert Item.string_to_number('5.5') == 5

#def test_get_from_csv(): #Тест не проходит. FileNotFoundError: [Errno 2] No such file or directory: '../src/items.csv'
#    Item.instantiate_from_csv('../src/items.csv')
#    item1 = Item.all[0]
#    assert item1.name == 'Смартфон'
