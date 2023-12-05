from item2 import Item

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

    