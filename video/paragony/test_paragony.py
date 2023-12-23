from paragony import get_price


def test_get_price():
    assert get_price(123) == '1.23'
    assert get_price(23) == '0.23'
    assert get_price(3) == '0.03'
    assert get_price(100) == '1.00'
    assert get_price(0) == '0.00'


def test_get_price_negative():
    assert get_price(-123) == '-1.23'
