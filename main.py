from grid.mesh.mesh import Mesh
from grid.domain import Domain
from solvers.numeric.euler import EulerMethod
from solvers.numeric.crank_nicholson import CrankNicholson
from solvers.exact.analytical import AnalyticalSolution

import matplotlib.pyplot as plt

from configuration.config import n, h, space_interval, time_interval

import numpy as np


def main():

    space = Mesh(n, space_interval[0], space_interval[1])
    time = Mesh(h, time_interval[0], time_interval[1])

    domain = Domain(space=space,
                    time=time)

    F = np.zeros((n - 2, h))

    for t in range(h):
        vec = domain.get_load(domain.time(t))
        for s in range(n - 2):
            F[s, t] = vec[s]

    numeric = EulerMethod()
    exact = AnalyticalSolution()

    U = numeric.solve(domain)
    E = exact.solve(domain)

    # Heatmap of numerical solution
    fig, ax = plt.subplots()
    im = ax.imshow(U, aspect='auto', extent=[time_interval[0], time_interval[1], space_interval[0], space_interval[1]])
    ax.set(xlabel='t', ylabel='x', title='Numerical Solution, dt=1/{}, dx=1/{}'.format(h - 1, n - 1))
    fig.colorbar(im)
    fig.savefig("heatmap.png")
    plt.show()

    # Plot of numerical and exact solutions at t=1
    fig, ax = plt.subplots()
    ax.plot(space.partition, U[:, -1], label='Numerical Solution')
    ax.plot(space.partition, E[:, -1], label='Analytical Solution')
    ax.set(xlabel='x', ylabel='Heat', title='Solution at t=1. dt=1/{}, dx=1/{}'.format(h - 1, n - 1))
    ax.legend()
    ax.grid()
    fig.savefig("finalSolutionPlot.png")
    plt.show()


if __name__ == '__main__':
    main()
