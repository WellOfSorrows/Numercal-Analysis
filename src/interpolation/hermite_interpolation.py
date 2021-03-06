import numpy as np


def hermite_interpolation(x_points: np.array, y_points: np.array, dy_points: np.array):
    """
    :return: The hermite coefficients.
    """

    x = x_points
    y = y_points
    dy = dy_points

    if len(x) != len(y) != len(dy):
        print("The vectors must be of the same length.")
        return None

    n = len(x)
    q = np.zeros((2*n, 2*n))
    z = np.zeros(2*n)

    for i in range(n):
        z[2 * i], z[2 * i + 1] = x[i], x[i]
        q[2 * i][0], q[2 * i + 1][0] = y[i], y[i]
        q[2 * i + 1][1] = dy[i]
        if i != 0:
            q[2 * i][1] = (q[2 * i][0] - q[2 * i - 1][0]) / (z[2 * i] - z[2 * i - 1])

    for i in range(2, 2*n):
        for j in range(2, i+1):
            q[i][j] = (q[i][j-1] - q[i-1][j-1]) / (z[i] - z[i-j])

    v = np.zeros(2*n)
    for i in range(2*n):
        v[i] = q[i][i]
    return v
