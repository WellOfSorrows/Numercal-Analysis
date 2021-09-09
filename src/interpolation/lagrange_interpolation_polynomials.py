import numpy as np


def lagrange_interpolation(point_to_eval, x_values: np.array, y_values: np.array):
    z = point_to_eval
    x = x_values
    y = y_values

    if len(x) != len(y):
        print("The vectors x_values & y_values must be of the same length.")
        return None

    p = 0
    n = len(x)
    w = np.ones(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                w[i] = (z - x[j])/(x[i] - x[j])*w[i]
        p += w[i] * y[i]

    return p

