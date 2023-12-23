from receipts.receipt import Receipt, random_receipt
from receipts.client import Client
from receipts.receipt_position import ReceiptPosition
from receipts.item import Item
from receipts.price import Price
import pytest
 
 
def test_client_regular():
    client = Client("Michal", 117891)
 
    assert client.name == "Michal"
 
    assert client.user_id == "117891"
 
    assert client.receipts == None
 
 
def test_client_add_receipt():
    client = Client("Michal", 117891)
 
    assert client.receipts == None
 
    
    receipt1 = Receipt([ReceiptPosition(1, Item("Milk", Price(100)))])
    receipt2 = Receipt([ReceiptPosition(2, Item("Banana", Price(200)))])
 
    client.add_receipt(receipt1)
    client.add_receipt(receipt2)
 
    assert client.receipts == [receipt1, receipt2]
 
 
# def test_client_spending():
#     client = Client("Michal", 117891)
 
#     assert client.receipts == None
 
#     receipt1: Receipt = random_receipt()
#     receipt2: Receipt = random_receipt()
 
#     client.add_receipt(receipt1)
#     client.add_receipt(receipt2)
 
#     assert client.receipts == [receipt1, receipt2]
 
#     assert (
#         client.total_spending.value_gr
#         == receipt1.total_price.value_gr + receipt2.total_price.value_gr
#     )
 
 
def test_client_bad_name():
    with pytest.raises(ValueError):
        Client("", "7382fb")
 
 
def test_client_bad__user_id():
    with pytest.raises(ValueError):
        Client("Michal", "")
 
 
def test_bad_receipt():
    client = Client("Michal", "7382fb")
 
    with pytest.raises(TypeError):
        client.add_receipt(1767)


def test_client_init():
    new_client = Client("Kamil", 12)
    assert new_client.name == "Kamil"
    assert new_client.user_id == '12'
    assert new_client.receipts == None
 
 
def test_client_init_empty_name():
    with pytest.raises(ValueError):
        Client("", 1)

 
 
def test_get_name():
    new_client = Client("Michał", 997)
    assert new_client.name == "Michał"
 

def test_str():
    new_client = Client("Jan Kowalski", 8)
    assert str(new_client) == "Client Jan Kowalski has id: 8."
