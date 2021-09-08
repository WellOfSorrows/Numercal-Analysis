import numpy as np


def ldl_factorization(dimensions, matrix: np.array):
    """This piece of code assumes that the lower matrix has the diagonal of identity matrix"""

    n = dimensions
    a = matrix

    lower = np.zeros((n, n))
    v = np.zeros(n)
    d = np.ones(n)

    for i in range(n):
        lower[i][i] = 1

    for i in range(n):
        for j in range(i):
            v[j] = lower[i][j] * d[j]

        sum_of = 0
        for j in range(i):
            sum_of += lower[i][j] * v[j]
        d[i] = a[i][i] - sum_of

        for j in range(i, n):
            sum_of = 0
            for k in range(i):
                sum_of += lower[j][k] * v[k]
            lower[j][i] = (a[j][i] - sum_of) / d[i]

    return lower, d
