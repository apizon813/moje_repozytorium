from items import Item, Container, AboveLiftError
import pytest

def test_item_create():
    item = Item('rock', 3)
    assert item.name == 'rock'
    assert item.mass == 3

def test_item_create_empty_name():
    item = Item('', 3)
    assert item.name == 'Mass'

def test_item_create_negative_mass():
    with pytest.raises(ValueError):
        Item('rock', -1)

def test_item_repr():
    item = Item('rock', 3)
    assert repr(item) == "Item(name=rock, mass=3)"


def test_conatiner_create():
    container = Container('box', 1, 10)
    assert container.name == 'box'
    assert container.mass == 1
    assert container.max_lift == 10

def test_container_create_empty_name():
    container = Container('', 1, 10)
    assert container.name == 'Box'

def test_container_create_negative_parameters():
    with pytest.raises(ValueError):
        Container('box', -1, 10)
    with pytest.raises(ValueError):
        Container('box', 1, -3)

def test_container_insert_item():
    item = Item('rock', 3)
    container = Container('box', 1, 10)
    container.insert(item)
    assert container.max_lift == 10
    assert container.current_lift == 7
    assert container.contains == [Item(name='rock', mass=3)]

def test_container_insert_above_max_lift():
    item = Item('rock', 11)
    container = Container('box', 1, 10)
    with pytest.raises(AboveLiftError):
        container.insert(item)

def test_container_insert_two_items():
    item1 = Item('rock', 3)
    item2 = Item('stick', 2)
    container = Container('box', 1, 10)
    container.insert(item1)
    container.insert(item2)
    assert container.max_lift == 10
    assert container.current_lift == 5
    assert container.contains == [Item(name='rock', mass=3), Item(name='stick', mass=2)]

def test_container_remove_item():
    item1 = Item('rock', 3)
    item2 = Item('stick', 2)
    container = Container('box', 1, 10)
    container.insert(item1)
    container.insert(item2)
    container.remove(item1)
    assert container.current_lift == 8
    assert container.contains == [Item(name='stick', mass=2)]

def test_container_remove_invalid_item():
    item1 = Item('rock', 3)
    item2 = Item('stick', 2)
    item3 = Item('bread', 1)
    container = Container('box', 1, 10)
    container.insert(item1)
    container.insert(item2)
    with pytest.raises(ValueError):
        container.remove(item3)

def test_container_info():
    item1 = Item('rock', 3)
    item2 = Item('stick', 2)
    container = Container('box', 1, 10)
    container.insert(item1)
    container.insert(item2)
    assert container.info == [3, 2]