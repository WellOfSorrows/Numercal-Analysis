import numpy as np


def lu_factorization(dimensions, matrix: np.array):
    """This piece of code assumes that the lower matrix has the diagonal of identity matrix"""

    n = dimensions
    a = matrix

    u = np.zeros((n, n))
    l = np.zeros((n, n))

    for i in range(n):
        l[i][i] = 1

    u[0][0] = a[0][0] / l[0][0]
    if l[0][0] * u[0][0] == 0:
        print('Factorization impossible')
        return None

    for j in range(1, n):
        u[0][j] = a[0][j] / l[0][0]
        l[j][0] = a[j][0] / u[0][0]

    for i in range(1, n):
        sum_of = 0
        for k in range(0, i, 1):
            sum_of += l[i][k] * u[k][i]
        u[i][i] = a[i][i] - sum_of

        if u[i][i] == 0:
            print('Factorization impossible')
            return None
        for j in range(i+1, n, 1):
            sum_of = 0
            for k in range(0, i, 1):
                sum_of += l[i][k] * u[k][j]
            u[i][j] = a[i][j] - sum_of

            sum_of = 0
            for k in range(0, i, 1):
                sum_of += l[j][k] * u[k][i]
            l[j][i] = (a[j][i] - sum_of) / u[i][i]

    sum_of = 0
    for k in range(0, n-1, 1):
        sum_of += l[n-1][k] * u[k][n-1]
    u[n-1][n-1] = a[n-1][n-1] - sum_of

    return l, u


def solve_lower(dimensions, lower_triangular: np.array, ans_vector: np.array):
    n = dimensions
    l = lower_triangular
    b = ans_vector

    y = np.zeros(n)

    y[0] = b[0] / l[0][0]

    for i in range(1, n):
        sum_of = 0
        for j in range(0, i, 1):
            sum_of += l[i][j] * y[j]
        y[i] = b[i] - sum_of

    return y


def solve_upper(dimensions, upper_triangular: np.array, ans_vector: np.array):
    n = dimensions
    u = upper_triangular
    y = ans_vector

    x = np.zeros(n)

    x[n-1] = y[n-1] / u[n-1][n-1]

    for i in range(n-2, 0, -1):
        sum_of = 0
        for j in range(i+1, n, 1):
            sum_of += u[i][j] * x[j]
        x[i] = (y[i] - sum_of) / u[i][i]

    return x
