from receipts.receipt import Receipt
from receipts.receipt_position import ReceiptPosition
from receipts.item import Item
from receipts.price import Price
from datetime import date
import pytest


def test_create_empty_receipt():
    paragon = Receipt()
    assert paragon.date == date.today()
    assert not paragon.positions
    assert paragon.total_price.value_gr == 0


def test_positions():
    milk = Item("Milk", Price(100))
    position1 = ReceiptPosition(1, milk)
    positions = [position1]
    receipt = Receipt(positions)
    assert receipt.positions == positions

def test_total_price():
    milk = Item("Milk", Price(100))
    position1 = ReceiptPosition(1, milk)
    positions = [position1]
    receipt = Receipt(positions)
    assert receipt.total_price == Price(100)


def test_create_receipt():
    item1 = ReceiptPosition(2, Item("banan", Price(300)))
    item2 = ReceiptPosition(3, Item("jablko", Price(200)))
    positions = [item1, item2]
    paragon = Receipt(positions)
    assert paragon.positions == positions
    # assert paragon.total_price == Price(1200)


def test__iter__():
    item1 = ReceiptPosition(2, Item("banan", Price(300)))
    item2 = ReceiptPosition(3, Item("jablko", Price(200)))
    positions = [item1, item2]
    paragon = Receipt(positions)
    for index, position in enumerate(paragon):
        assert position == paragon.positions[index]


def test__len__():
    item1 = ReceiptPosition(2, Item("banan", Price(300)))
    item2 = ReceiptPosition(3, Item("jablko", Price(200)))
    positions = [item1, item2]
    paragon = Receipt(positions)
    assert len(paragon) == len(positions)


def test_len_empty_receipt():
    paragon = Receipt()
    assert len(paragon) == 0


def test_negative_top_expensive_positions():
    paragon = Receipt()
    with pytest.raises(ValueError):
        paragon.top_expensive_positions(-2)


def test_one_top_expensive_position():
    item1 = ReceiptPosition(2, Item("banan", Price(300)))
    item2 = ReceiptPosition(3, Item("jablko", Price(400)))
    positions = [item1, item2]
    paragon = Receipt(positions)
    assert paragon.top_expensive_positions() == [item2]


def test_two_expensive_positions():
    item1 = ReceiptPosition(2, Item("banan", Price(300)))
    item2 = ReceiptPosition(3, Item("jablko", Price(400)))
    item3 = ReceiptPosition(4, Item('gruszka', Price(500)))
    positions = [item1, item2, item3]
    paragon = Receipt(positions)
    assert paragon.top_expensive_positions(2) == [item3, item2]


def test_too_many_expensive_positions():
    item1 = ReceiptPosition(2, Item("banan", Price(300)))
    item2 = ReceiptPosition(3, Item("jablko", Price(400)))
    item3 = ReceiptPosition(4, Item('gruszka', Price(500)))
    positions = [item1, item2, item3]
    paragon = Receipt(positions)
    assert paragon.top_expensive_positions(4) == [item3, item2, item1]


def test_empty_expensive_positions():
    paragon = Receipt()
    assert not paragon.top_expensive_positions()



