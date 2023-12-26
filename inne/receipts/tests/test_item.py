from receipts.item import Item
import pytest


def test_init():
    item = Item('Milk', 200)
    assert item.name == 'Milk'
    assert item.price == 200
    assert item.barcode == '1234567890123'


def test_init_barcode_less_than_13_chars():
    with pytest.raises(ValueError):
        Item('Milk', 200, '123456789012')


def test_init_empty_name():
    with pytest.raises(ValueError):
        Item('', 200)


def test_str():
    item = Item('Milk', 200)
    assert str(item) == 'Milk price is 200, barcode is 1234567890123'


def test_repr():
    item = Item('Milk', 200)
    assert repr(item) == 'Item(name=Milk, price=200, barcode=1234567890123)'
