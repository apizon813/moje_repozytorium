from item2 import Item, Box

def test_item_init():
    item = Item("thing", mass=5)
    assert item.name == 'thing'
    assert item.mass == 5

def test_repr():
    item = Item("thing", mass=5)
    assert repr(item) == 'Item(name=thing, mass=5)'

def test_eq_true():
    item1 = Item("thing", mass=5)
    item2 = Item("thing", mass=5)
    assert item1 == item2

def test_eq_false():
    item1 = Item("thing", mass=5)
    item2 = Item("stick", mass=2)
    assert not item1 == item2

def test_box_init():
    box = Box("container", mass=2, lift=10)
    assert box.name == 'container'
    assert box.mass == 2
    assert box.lift == 10
    assert box.current_lift == 10
    assert box.contains == []

def test_box_insert():
    item = Item("thing", mass=4)
    box = Box("container", mass=2, lift=10)
    box.insert(item)
    assert box.current_lift == 6
    assert box.contains == [item]

def test_box_remove():
    pass