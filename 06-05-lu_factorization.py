import numpy as np


def lu_factorization(dimensions, matrix: np.array):
    """This piece of code assumes that the lower matrix has the diagonal of identity matrix"""

    n = dimensions
    a = matrix

    upper = np.zeros((n, n))
    lower = np.zeros((n, n))

    for i in range(n):
        lower[i][i] = 1

    upper[0][0] = a[0][0] / lower[0][0]
    if lower[0][0] * upper[0][0] == 0:
        print('Factorization impossible')
        return None

    for j in range(1, n):
        upper[0][j] = a[0][j] / lower[0][0]
        lower[j][0] = a[j][0] / upper[0][0]

    for i in range(1, n):
        sum_of = 0
        for k in range(0, i, 1):
            sum_of += lower[i][k] * upper[k][i]
        upper[i][i] = a[i][i] - sum_of

        if upper[i][i] == 0:
            print('Factorization impossible')
            return None
        for j in range(i+1, n, 1):
            sum_of = 0
            for k in range(0, i, 1):
                sum_of += lower[i][k] * upper[k][j]
            upper[i][j] = a[i][j] - sum_of

            sum_of = 0
            for k in range(0, i, 1):
                sum_of += lower[j][k] * upper[k][i]
            lower[j][i] = (a[j][i] - sum_of) / upper[i][i]

    sum_of = 0
    for k in range(0, n-1, 1):
        sum_of += lower[n-1][k] * upper[k][n-1]
    upper[n-1][n-1] = a[n-1][n-1] - sum_of

    return lower, upper


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
