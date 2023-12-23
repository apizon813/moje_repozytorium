import pytest

from polynomial import Polynomial
from errors import NegativeDegreeError, RepeatedTermError, ZeroCoefficientError


def test_term_to_string_degree_over_one():
    polynomial = Polynomial()
    assert polynomial._term_to_string(2, 5) == "+5x^2"
    assert polynomial._term_to_string(3, 1) == "+x^3"
    assert polynomial._term_to_string(2, -1) == "-x^2"


def test_term_to_string_degree_one():
    polynomial = Polynomial()
    assert polynomial._term_to_string(1, 2) == "+2x"
    assert polynomial._term_to_string(1, -2) == "-2x"
    assert polynomial._term_to_string(1, -1) == "-x"
    assert polynomial._term_to_string(1, 1) == "+x"


def test_term_to_string_degree_zero():
    polynomial = Polynomial()
    assert polynomial._term_to_string(0, 1) == "+1"
    assert polynomial._term_to_string(0, -8) == "-8"


def test_create_empty_polynomial():
    polynomial = Polynomial()
    assert polynomial.__str__() == "0"


def test_create_0_degree_polynomial():
    polynomial = Polynomial([(0, -8)])
    assert polynomial.__str__() == "-8"


def test_create_1_degree_polynomial():
    polynomial = Polynomial([(0, 4), (1, -2)])
    assert polynomial.__str__() == "-2x+4"


def test_create_5_degree_polynomial():
    polynomial = Polynomial([(1, 5), (3, 2), (5, -1)])
    assert polynomial.__str__() == "-x^5+2x^3+5x"


def test_create_6_degree_polynomial():
    polynomial = Polynomial([(4, 2), (6, 3), (2, 3), (0, 7)])
    assert polynomial.__str__() == "3x^6+2x^4+3x^2+7"


def test_create_polynomial_with_repeated_term():
    with pytest.raises(RepeatedTermError):
        Polynomial([(1, 5), (3, 0), (1, 5)])


def test_create_polynomial_with_term_coefficient_equals_zero():
    with pytest.raises(ZeroCoefficientError):
        Polynomial([(1, 5), (3, 0), (5, -1)])


def test_create_polynomial_with_negative_term_degree():
    with pytest.raises(NegativeDegreeError):
        Polynomial([(1, 5), (-3, 7), (5, -1)])


def test_polynomial_degree_empty():
    polynomial = Polynomial([])
    assert polynomial.degree() is None


def test_polynomial_degree_zero():
    polynomial = Polynomial([(0, 7)])
    assert polynomial.degree() == 0


def test_polynomial_degree_two():
    polynomial = Polynomial([(2, 7)])
    assert polynomial.degree() == 2


def test_polynomial_degree_complex():
    polynomial = Polynomial([(4, 2), (6, 3), (2, 3), (0, 7)])
    assert polynomial.degree() == 6


def test_coefficient():
    polynomial = Polynomial([(7, 2), (3, 8), (2, 3), (0, -5)])
    assert polynomial.coefficient(8) == 0
    assert polynomial.coefficient(7) == 2
    assert polynomial.coefficient(6) == 0
    assert polynomial.coefficient(5) == 0
    assert polynomial.coefficient(4) == 0
    assert polynomial.coefficient(3) == 8
    assert polynomial.coefficient(2) == 3
    assert polynomial.coefficient(1) == 0
    assert polynomial.coefficient(0) == -5


def test_polynominal_value():
    polynomial = Polynomial([(3, 8), (2, 3), (0, -5)])
    assert polynomial.value(0) == -5
    assert polynomial.value(1) == 6
    assert polynomial.value(-2) == -64 + 12 - 5


def test_polynomial_add_equal_lengths():
    polynomial1 = Polynomial([(7, 2), (3, 3), (2, 3), (0, -5)])
    polynomial2 = Polynomial([(5, 3), (2, -3), (1, -3), (0, 7)])
    result = polynomial1.add(polynomial2)
    assert result.__str__() == "2x^7+3x^5+3x^3-3x+2"


def test_polynomial_add_first_shorter():
    polynomial1 = Polynomial([(7, 2), (3, 3)])
    polynomial2 = Polynomial([(5, 3), (2, -3), (1, -3), (0, 7)])
    result = polynomial1.add(polynomial2)
    assert result.__str__() == "2x^7+3x^5+3x^3-3x^2-3x+7"


def test_polynomial_add_second_shorter():
    polynomial1 = Polynomial([(7, 2), (3, 3), (2, 3), (0, -5)])
    polynomial2 = Polynomial([(5, 3), (3, -3)])
    result = polynomial1.add(polynomial2)
    assert result.__str__() == "2x^7+3x^5+3x^2-5"


def test_polynomial_add_zero_right():
    polynomial1 = Polynomial([(7, 2), (3, 3), (2, 3), (0, -5)])
    polynomial2 = Polynomial([])
    result = polynomial1.add(polynomial2)
    assert result.__str__() == "2x^7+3x^3+3x^2-5"


def test_polynomial_add_zero_left():
    polynomial1 = Polynomial([])
    polynomial2 = Polynomial([(7, 2), (3, 3), (2, 3), (0, -5)])
    result = polynomial1.add(polynomial2)
    assert result.__str__() == "2x^7+3x^3+3x^2-5"


def test_polynomial_add_result_zero():
    polynomial1 = Polynomial([(7, 2), (3, 3), (2, 3), (0, -5)])
    polynomial2 = Polynomial([(7, -2), (3, -3), (2, -3), (0, 5)])
    result = polynomial1.add(polynomial2)
    assert result.__str__() == "0"


def test_polynomial_subtract_equal_lengths():
    polynomial1 = Polynomial([(7, 2), (3, 3), (2, 3), (0, -5)])
    polynomial2 = Polynomial([(5, 3), (2, 3), (1, -3), (0, 7)])
    result = polynomial1.subtract(polynomial2)
    assert result.__str__() == "2x^7-3x^5+3x^3+3x-12"


def test_polynomial_subtract_first_shorter():
    polynomial1 = Polynomial([(7, 2), (3, 3)])
    polynomial2 = Polynomial([(5, 3), (2, -3), (1, -3), (0, 7)])
    result = polynomial1.subtract(polynomial2)
    assert result.__str__() == "2x^7-3x^5+3x^3+3x^2+3x-7"


def test_polynomial_subtract_second_shorter():
    polynomial1 = Polynomial([(7, 2), (3, 3), (2, 3), (0, -5)])
    polynomial2 = Polynomial([(5, 3), (3, -3)])
    result = polynomial1.subtract(polynomial2)
    assert result.__str__() == "2x^7-3x^5+6x^3+3x^2-5"


def test_polynomial_subtract_zero():
    polynomial1 = Polynomial([(7, 2), (3, 3), (2, 3), (0, -5)])
    polynomial2 = Polynomial([])
    result = polynomial1.subtract(polynomial2)
    assert result.__str__() == "2x^7+3x^3+3x^2-5"


def test_polynomial_subtract_from_zero():
    polynomial1 = Polynomial([])
    polynomial2 = Polynomial([(7, 2), (3, 3), (2, 3), (0, -5)])
    result = polynomial1.subtract(polynomial2)
    assert result.__str__() == "-2x^7-3x^3-3x^2+5"


def test_polynomial_subtract_result_zero():
    polynomial1 = Polynomial([(7, 2), (3, 3), (2, 3), (0, -5)])
    polynomial2 = Polynomial([(7, 2), (3, 3), (2, 3), (0, -5)])
    result = polynomial1.subtract(polynomial2)
    assert result.__str__() == "0"
