from zad1 import substring


def test_substring_work():
    assert substring([0, 1, 2], 2) == [1, 2]


def test_substring_long():
    assert substring([6, 8, 2, 87, 123, 432, 3, 7, 9], 3) == [87, 123, 432]
    assert substring([-3, 23, -3, 56565, -444, 22, 0], 3) == [23, -3, 56565]
