import numpy as np


def horner_method(degree, coefficients: np.array, initial_point):
    n = degree
    a = coefficients  # must be of the size n+1
    x_0 = initial_point

    y = a[n]
    z = a[n]

    for i in range(n-1, 0, -1):
        y = x_0 * y + a[i]
        z = x_0 * z + y

    y = x_0 * y + a[0]
    return y, z
