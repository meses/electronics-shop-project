import pytest
from src.keyboard import KeyBoard
from src.item import Item

@pytest.fixture
def keyboard1():
    return KeyBoard("Razer", 10000, 20)

def test_init(keyboard1):
    assert keyboard1.name == "Razer"
    assert keyboard1.language == "EN"
    assert str(keyboard1) == "Razer"

def test_change_lang(keyboard1):
    keyboard1.change_lang()
    assert str(keyboard1.language) == "RU"