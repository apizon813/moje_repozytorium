from sympy import (
    IndexedBase,
    Idx,
    Sum,
    cos,
)
from math import pi, sqrt


def quadratic():
    x = IndexedBase('x')
    function = x[1] ** 2
    return function


def rastrigin(d):
    x = IndexedBase('x')
    i = Idx('i', (1, d))
    function = 10 * d + Sum(x[i] ** 2-10*cos(2 * pi * x[i]), [i, 1, d])
    function = function.subs(d, d).doit()
    return function


def griewank():
    x = IndexedBase('x')
    i = Idx('i', (1, 2))
    function = Sum(x[i] ** 2 / 4000, [i, 1, 2]) - \
        cos(x[1]) * cos(x[2] / sqrt(2)) + 1
    return function.doit()
