from item2 import Item

def test_item_init():
    item = Item("thing", mass=5)
    assert item.name == 'thing'
    assert item.mass == 5