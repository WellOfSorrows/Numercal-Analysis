import numpy as np


def crout_factorization(dimensions, matrix: np.array):
    n = dimensions
    a = matrix

    lower = np.zeros((n, n))
    u = np.zeros((n, n))
    z = np.zeros(n)

    lower[0][0] = a[0][0]
    u[0][1] = a[0][1] / lower[0][0]
    z[0] = a[0][n] / lower[0][0]

    for i in range(1, n - 1):
        lower[i][i - 1] = a[i][i - 1]
        lower[i][i] = a[i][i] - lower[i][i - 1] * u[i - 1][i]
        u[i][i + 1] = a[i][i + 1] / lower[i][i]
        z[i] = (a[i][n] - lower[i][i - 1] * z[i - 1]) / lower[i][i]

    lower[n - 1][n - 2] = a[n - 1][n - 2]
    lower[n - 1][n - 1] = a[n - 1][n - 1] - lower[n - 1][n - 2] * u[n - 2][n - 1]
    z[n - 1] = (a[n - 1][n] - lower[n - 1][n - 2] * z[n - 2]) / lower[n - 1][n - 1]

    x = z
    for i in range(n - 2, -1, -1):
        x[i] = z[i] - u[i][i + 1] * x[i + 1]

    return x

#
# def main():
#     n = 4
#     a = np.array([[2, -1, 0, 0, 1],
#                   [-1, 2, -1, 0, 0],
#                   [0, -1, 2, -1, 0],
#                   [0, 0, -1, 2, 1]])
#     result = crout_factorization(n, a)
#     print(result)
#
#
# if __name__ == '__main__':
#     main()
