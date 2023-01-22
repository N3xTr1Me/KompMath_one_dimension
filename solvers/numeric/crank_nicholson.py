import numpy as np

from solvers.numeric.euler import EulerMethod
from configuration.config import is_explicit
from grid.domain import Domain


class CrankNicholson(EulerMethod):
    def __init__(self, mode: bool = is_explicit):
        super(CrankNicholson, self).__init__(mode)

    def solve(self, domain: Domain) -> np.ndarray:
        self._domain = domain

        result = np.zeros((domain.space_steps(), domain.time_steps()))
        C = np.zeros((domain.space_steps() - 2, domain.time_steps()))

        for t in range(domain.time_steps() - 1):
            first = super(CrankNicholson, self)._forward(current_step=C[:, t], t=t, dt=domain.dt())
            second = super(CrankNicholson, self)._backward(current_step=C[:, t], t=t, dt=domain.dt())

            C[:, t + 1] = 0.5 * (first + second)

        result[1:-1] = C

        self._domain = None

        return result / domain.time_steps()

    # def __call__(self) -> np.ndarray:
    #     space_steps = self.__domain.space_steps()
    #     time_steps = self.__domain.time_steps()
    #     dt = self.__domain.dt()
    #
    #     M = self.__domain.build_M()  # mass matrix
    #     S = self.__domain._build_stiffness()  # stiffness matrix
    #     F = self.__domain.get_load()  # matrix of load vectors
    #
    #     result = np.zeros((space_steps, time_steps))  # final resulting matrix
    #     C = np.zeros((space_steps - 2, time_steps))  # computation matrix
    #
    #     for n in range(time_steps - 1):
    #         first = np.linalg.solve(M, dt * (F[:, n] - np.matmul(S, C[:, n]))) + C[:, n]
    #         second = np.linalg.solve(dt * M + S, F[:, n + 1] + dt * np.matmul(M, C[:, n]))
    #         C[:, n + 1] = 0.5 * (first + second)
    #
    #     result[1:-1] = C
    #
    #     return result
