from math import pi, exp, sin, cos, tan, sqrt


# number of steps in space partition
n = 100

# number of steps in time partition
h = 1000

# space partition boundary conditions
space_interval = (0, 8)

# time partition boundary conditions
time_interval = (0, 9)

# explicit / implicit method switch
is_explicit = False


# difference function used in calculations
def f(x: float, t: float) -> float:
    return ((pi ** 2) - 1) * exp(-t) * sin(pi * x)


# original function used for analytical solution
def u(x: float, t: float) -> float:
    return exp(-t) * sin(pi * x)
