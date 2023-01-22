from math import pi, exp, sin, cos, tan, sqrt


# number of steps in space partition
n = 11

# number of steps in time partition
h = 552 * 6

# space partition boundary conditions
space_interval = (0, 1)

# time partition boundary conditions
time_interval = (0, 5)

# explicit / implicit method switch
is_explicit = False


# difference function used in calculations
def f(x: float, t: float) -> float:
    return ((pi ** 2) - 1) * exp(-t) * sin(pi * x)
    # return (x**2 * exp(- x**2 / (4 * t))) / (16 * pi * t**3) - \
    #        ((x**2 * exp(- x**2 / (4 * t))) / (4 * t**2) -
    #         (exp(-x**2 / (4 * t))) / (2 * t)) / (4 * pi * t) - \
    #        (exp(-x ** 2 / (4 * t))) / (4 * pi * t**2)


# original function used for analytical solution
def u(x: float, t: float) -> float:
    return exp(-t) * sin(pi * x)
    # return 1 / (4 * pi * t) * exp(- x**2 / (4 * t))
