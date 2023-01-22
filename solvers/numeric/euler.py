from solvers.solver import ISolver
from configuration.config import is_explicit
from grid.domain import Domain

import numpy as np


class EulerMethod(ISolver):
    def __init__(self, mode: bool = is_explicit):
        self.__mode = mode
        self._domain = None

    def _derivative(self, current_step: np.ndarray, t: float) -> np.ndarray:
        B = (self._domain.M + self._domain.dt() / 2 * self._domain.S)
        A = (self._domain.M - self._domain.dt() / 2 * self._domain.S)

        return np.linalg.inv(B) @ ((A - B) @ current_step + self._domain.get_load(t=t)) / self._domain.dt()

    def _forward(self, current_step: np.ndarray, t: int, dt: float) -> np.ndarray:
        return current_step + dt * self._derivative(current_step, self._domain.time(t))

    def _backward(self, current_step: np.ndarray, t: int, dt: float) -> np.ndarray:
        return current_step + dt * self._derivative(current_step, self._domain.time(t + 1))

    def solve(self, domain: Domain) -> np.ndarray:
        self._domain = domain
        dt = self._domain.dt()

        C = np.zeros((self._domain.space_steps() - 2, self._domain.time_steps()))
        result = np.zeros((domain.space_steps(), domain.time_steps()))  # final resulting matrix

        for t in range(self._domain.time_steps() - 1):
            if self.__mode:
                C[:, t + 1] = self._forward(current_step=C[:, t], t=t, dt=domain.dt())
            else:
                C[:, t + 1] = self._backward(current_step=C[:, t], t=t, dt=domain.dt())

        result[1:-1] = C

        self._domain = None

        return result * domain.dt()
