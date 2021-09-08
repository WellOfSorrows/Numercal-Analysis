import numpy as np
from math import sqrt


def cholesky_factorization(dimensions, matrix: np.array):
    n = dimensions
    a = matrix

    lower = np.zeros((n, n))
    lower[0][0] = sqrt(a[0][0])

    for j in range(1, n):
        lower[j][0] = a[j][0] / lower[0][0]
    for i in range(1, n-1):
        sum_of = 0
        for k in range(i):
            sum_of += lower[i][k] ** 2
        lower[i][i] = sqrt(a[i][i] - sum_of)

        for j in range(i+1, n):
            sum_of = 0
            for k in range(i):
                sum_of += lower[i][k] * lower[j][k]
            lower[j][i] = (a[j][i] - sum_of) / lower[i][i]

    sum_of = 0
    for k in range(n):
        sum_of += lower[n-1][k] ** 2
    lower[n-1][n-1] = sqrt(a[n-1][n-1] - sum_of)

    return lower


def main():
    dimensions = 3
    matrix = np.array([[4, -1, 1],
                       [-1, 4.25, 2.75],
                       [1, 2.75, 3.5]])
    result = cholesky_factorization(dimensions, matrix)
    print(result)


if __name__ == '__main__':
    main()


