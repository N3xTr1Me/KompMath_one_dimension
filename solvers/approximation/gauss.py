from math import sqrt

from solvers.approximation.approximation import IApproximation
from configuration.config import f


# Gaussian two-point quadrature approximation
class GaussQuadrature(IApproximation):
    _left = -sqrt(1/3)
    _right = sqrt(1/3)

    def __init__(self, rhs: callable = f):
        self.__f = rhs

    def __call__(self, x: float, t: float, h: float) -> float:
        a = x - h / 2
        b = x + h / 2

        return (self.__f(x=((b - a) * self._left + a + b) / 2, t=t) +
                self.__f(x=((b - a) * self._right + a + b) / 2, t=t)) * (b - a) / 2
