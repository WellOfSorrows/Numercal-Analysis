import numpy as np
from math import sqrt


def cholesky_factorization(dimensions, matrix: np.array):
    n = dimensions
    a = matrix

    l = np.zeros((n, n))
    l[0][0] = sqrt(a[0][0])

    for j in range(1, n):
        l[j][0] = a[j][0] / l[0][0]
    for i in range(1, n-1):
        sum_of = 0
        for k in range(i):
            sum_of += l[i][k] ** 2
        l[i][i] = sqrt(a[i][i] - sum_of)

        for j in range(i+1, n):
            sum_of = 0
            for k in range(i):
                sum_of += l[i][k] * l[j][k]
            l[j][i] = (a[j][i] - sum_of) / l[i][i]

    sum_of = 0
    for k in range(n):
        sum_of += l[n-1][k] ** 2
    l[n-1][n-1] = sqrt(a[n-1][n-1] - sum_of)

    return l
