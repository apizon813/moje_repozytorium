import cheapcalc_tools
import pytest


def test_cheapcalc_tools_add():
    assert cheapcalc_tools.add(1, 2) == 3
    assert cheapcalc_tools.add(1.2, 3.4) == 4.6
    assert cheapcalc_tools.add(1.2, 3) == 4.2
    assert cheapcalc_tools.add(0.1, 0.2) == pytest.approx(0.3)
    try:
        cheapcalc_tools.add('asd', 1) == 0
        assert False
    except TypeError:
        assert True


def test_cheapcalc_tools_subtrack():
    assert cheapcalc_tools.subtract(1, 1) == 0
    assert cheapcalc_tools.subtract(-5, -3) == -2
    assert cheapcalc_tools.subtract(-3.4, -1.2) == -2.2
    
def test_cheapcalc_tools_multiply():
    assert cheapcalc_tools.multiply(2, 3) == 6
    assert cheapcalc_tools.multiply(0.3, 1/3) == pytest.approx(0.1)
    assert cheapcalc_tools.multiply(0, 0) == 0

def test_asd():
    with pytest.raises(ZeroDivisionError):
        assert cheapcalc_tools.divide(1, 0)