import numpy as np


def crout_factorization(dimensions, matrix: np.array):
    n = dimensions
    a = matrix

    l = np.zeros((n, n))
    u = np.zeros((n, n))
    z = np.zeros(n)

    l[0][0] = a[0][0]
    u[0][1] = a[0][1] / l[0][0]
    z[0] = a[0][n] / l[0][0]

    for i in range(1, n - 1):
        l[i][i - 1] = a[i][i - 1]
        l[i][i] = a[i][i] - l[i][i - 1] * u[i - 1][i]
        u[i][i + 1] = a[i][i + 1] / l[i][i]
        z[i] = (a[i][n] - l[i][i - 1] * z[i - 1]) / l[i][i]

    l[n - 1][n - 2] = a[n - 1][n - 2]
    l[n - 1][n - 1] = a[n - 1][n - 1] - l[n - 1][n - 2] * u[n - 2][n - 1]
    z[n - 1] = (a[n - 1][n] - l[n - 1][n - 2] * z[n - 2]) / l[n - 1][n - 1]

    x = z
    for i in range(n - 2, -1, -1):
        x[i] = z[i] - u[i][i + 1] * x[i + 1]

    return x
