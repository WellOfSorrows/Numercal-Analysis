import numpy as np


def ldlt_factorization(dimensions, matrix: np.array):
    """This piece of code assumes that the lower matrix has the diagonal of identity matrix"""

    n = dimensions
    a = matrix

    l = np.zeros((n, n))
    v = np.zeros(n)
    d = np.ones(n)

    for i in range(n):
        l[i][i] = 1

    for i in range(n):
        for j in range(i):
            v[j] = l[i][j] * d[j]

        sum_of = 0
        for j in range(i):
            sum_of += l[i][j] * v[j]
        d[i] = a[i][i] - sum_of

        for j in range(i, n):
            sum_of = 0
            for k in range(i):
                sum_of += l[j][k] * v[k]
            l[j][i] = (a[j][i] - sum_of) / d[i]

    return l, d
