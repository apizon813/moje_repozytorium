from sympy import (
    IndexedBase,
    diff,
)
from math import sqrt


class Function():
    def __init__(self, function, dimensions):
        self.dim = dimensions
        self.fun = function
        self.vars = self.get_variables()
        self.grad = self.gradient()

    def get_variables(self):
        variables = []
        x = IndexedBase('x')
        for i in range(self.dim):
            variable = x[i+1]
            variables += [variable]
        return tuple(variables)

    def gradient(self):
        gradient = []
        for variable in self.vars:
            derivative = diff(self.fun, variable)
            gradient += [derivative]
        return tuple(gradient)

    def grad_eval(self, coords):
        gradient_value = []
        for i in range(self.dim):
            derivative = self.grad[i]
            for j in range(self.dim):
                variable = self.vars[j]
                derivative = derivative.subs(variable, coords[j])

            gradient_value += [derivative]
        return tuple(gradient_value)


class Solver():
    def __init__(self, fun, dim, x0, beta):
        self.J = Function(fun, dim)
        self.dim = dim
        self.x0 = x0
        self.beta = beta
        self.current_step = 0
        self.x = x0
        self.data = {
            0: x0,
        }

    def step_till_stop(self, steps, trsh):
        if not self.current_step == 0:
            if self.trsh_reached(trsh):
                return self.data[self.current_step]
        while self.current_step < steps:
            self.step()
            if self.trsh_reached(trsh):
                return self.data[self.current_step]
        return self.data[self.current_step]

    def step(self):
        self.current_step += 1
        gradient = self.J.grad_eval(self.x)
        xnext = list(self.x)
        for i in range(self.dim):
            xnext[i] = self.x[i] - self.beta * gradient[i]
        self.x = tuple(xnext)
        self.data[self.current_step] = tuple(xnext)

    def trsh_reached(self, trsh):

        distance = self.eval_distance()
        if distance < trsh:
            return True
        return False

    def eval_distance(self):
        x1 = self.data[self.current_step]
        x2 = self.data[self.current_step - 1]
        sum = 0
        for i in range(self.dim):
            sum += (x1[i] - x2[i]) ** 2
        return sqrt(sum)
