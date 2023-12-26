from receipts.price import Price
import pytest


def test_price_typical():
    price = Price(300)
    assert price.value_gr == 300


def test_price_init_empty():
    price = Price()
    assert price.value_gr == 0


def test_price_init_with_negative():
    with pytest.raises(ValueError):
        Price(-200)


def test_price_init_float():
    price = Price(200.1)
    assert price.value_gr == 200


def test_price_in_str():
    price = Price("150")
    assert price.value_gr == 150


def test_price_in_str_with_letters():
    with pytest.raises(ValueError):
        Price("150zl")


def test_price_add_typical():
    price1 = Price(300)
    price2 = Price(200)
    assert (price1 + price2).value_gr == 500


def test_price_sub_typical():
    price1 = Price(300)
    price2 = Price(200)
    assert (price1 - price2).value_gr == 100


def test_price_mul_typical():
    price = Price(300)
    assert (price * 3).value_gr == 900


def test_price_rmul_typical():
    price = Price(300)
    assert (3 * price).value_gr == 900


def test_price_lt():
    price1 = Price(300)
    price2 = Price(200)
    assert not price1 < price2
    assert price2 < price1


def test_price_from_float():
    price = Price.from_float(4.20)
    assert price.value_gr == 420


def test_price_from_float_empty():
    price = Price.from_float()
    assert price.value_gr == 0


def test_price_from_float_negative():
    with pytest.raises(ValueError):
        Price.from_float(-2.13)


def test_price_from_float_string_with_only_numbers():
    price = Price.from_float("4.20")
    assert price.value_gr == 420


def test_price_from_float_string_with_not_only_numbers():
    with pytest.raises(ValueError):
        Price.from_float("4.20zl")


def test_price_to_str():
    price = Price(321)
    assert str(price) == "321"


def test_eq_true():
    p1 = Price(300)
    p2 = Price(300)
    assert p1.__eq__(p2)


def test_eq_false():
    p1 = Price(300)
    p2 = Price(400)
    assert not p1.__eq__(p2)


def test_format_price_typical():
    p1 = Price(345)
    assert p1._format_price() == "3.45"


def test_format_price_gr_less_than_10():
    p1 = Price(305)
    assert p1._format_price() == "3.05"


def test_format_price_zl_less_than_1():
    p1 = Price(45)
    assert p1._format_price() == "0.45"


def test_str():
    p1 = Price(345)
    assert str(p1) == p1.__str__()


def test_split_price_typical():
    p1 = Price(345)
    assert p1._split_price() == (3, 45)


def test_split_price_gr_less_than_10():
    p1 = Price(305)
    assert p1._split_price() == (3, 5)


def test_split_price_zl_less_than_1():
    p1 = Price(45)
    assert p1._split_price() == (0, 45)


def test_repr():
    p1 = Price(345)
    assert p1.__repr__() == "Price(value_gr=345)"
