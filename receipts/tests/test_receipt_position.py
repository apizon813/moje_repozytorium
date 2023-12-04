from receipts.receipt_position import ReceiptPosition
from receipts.item import Item
from receipts.price import Price
import pytest


def test_repr():
    item = Item("Milk", Price(100))
    position = ReceiptPosition(2, item)
    assert repr(position) == 'ReceiptPosition(amount=2, item=Item(name=Milk, price=100, barcode=1234567890123))'

# def test_item():
#     item = ReceiptPosition.item(2)
#     receipt_position = ReceiptPosition(4, item)
#     assert receipt_position.item() ==  2


# def test_amount_basic():
#     receipt_position = ReceiptPosition(4, 2)
#     assert receipt_position.amount() == 4.0


# def test_amount_is_positive():
#     receipt_position = ReceiptPosition(2.5, 9)
#     assert receipt_position.amount() == 2.5


# def test_amount_is_negative():
#     receipt_position = ReceiptPosition(-3.6, 9)
#     with pytest.raises(ValueError):
#         receipt_position.amount()