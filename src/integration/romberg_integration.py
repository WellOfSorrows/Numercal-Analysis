import numpy as np
from math import sin, pi, e


def romberg_integration(function, left_endpoint, right_endpoint, number):
    f = function
    a = left_endpoint
    b = right_endpoint
    n = number

    h = b - a
    r = np.zeros((2, n))
    r[0][0] = (h/2) * (f(a) + f(b))

    for i in range(1, n, 1):
        sum_of = 0
        for k in range(0, 2**(i-1), 1):
            sum_of += f(a + (k+1 - 0.5) * h)

        r[1][0] = (1/2) * (r[0][0] + h * sum_of)
        for j in range(1, i+1, 1):
            r[1][j] = r[1][j-1] + ((r[1][j-1] - r[0][j-1])/(4**j-1))

        h = h/2
        for j in range(0, i+1, 1):
            r[0][j] = r[1][j]

    return r[1][n-1]
