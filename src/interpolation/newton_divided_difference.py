import numpy as np


def newton_divided_difference(x_points: np.array, y_points: np.array):
    """
    :return: The complete interpolation table.
    """

    x = x_points
    y = y_points

    if len(x) != len(y):
        print("The vectors x_values & y_values must be of the same length.")
        return None

    n = len(x)
    v = np.zeros((n, n))
    for i in range(n):
        v[i][0] = y[i]

    for i in range(1, n):
        for j in range(1, i+1):
            v[i][j] = (v[i][j-1] - v[i-1][j-1]) / (x[i] - x[i-j])

    return v
