from sympy import (
    IndexedBase,
    Idx,
    Sum,
    cos,
)
from math import pi, sqrt


def rastrigin(d):
    x = IndexedBase('x')
    i = Idx('i', (1, d))
    function = 10 * d + Sum(x[i] ** 2-10*cos(2 * pi * x[i]), [i, 1, d])
    function = function.subs(d, d).doit()
    return function


def griewank(d):
    x = IndexedBase('x')
    i = Idx('i', (1, 2))
    function = Sum(x[i] ** 2 / 4000, [i, 1, 2]) - \
        cos(x[1]) * cos(x[2] / sqrt(2)) + 1
    return function.doit()


def drop_wave():
    x = IndexedBase('x')
    function = (1 + cos(12 * sqrt(x[1] ^ 2 + x[2] ^ 2))) / \
        (0.5 * (x[1] ^ 2 + x[2] ^ 2) + 2)
    return function.doit()
