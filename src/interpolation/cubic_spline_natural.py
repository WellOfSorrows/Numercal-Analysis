import numpy as np
from math import e


def cubic_spline_natural(number_of_splines, x_values: np.array, y_values: np.array):
    """
    :return: The natural cubic spline coefficients.
    """

    n = number_of_splines
    x = x_values
    a = y_values

    if len(x) != len(a):
        print("The vectors x_values & y_values must be of the same length.")
        return None

    h = np.zeros(n)
    for i in range(n):
        h[i] = x[i + 1] - x[i]

    alpha = np.zeros(n)
    for i in range(1, n, 1):
        alpha[i] = (3 / h[i]) * (a[i + 1] - a[i]) - (3 / h[i - 1]) * (a[i] - a[i - 1])

    p = np.ones(n + 1)
    r = np.zeros(n + 1)
    z = np.zeros(n + 1)

    for i in range(1, n, 1):
        p[i] = 2 * (x[i + 1] - x[i - 1]) - (h[i - 1] * r[i - 1])
        r[i] = h[i] / p[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / p[i]

    c = np.zeros(n)
    b = np.zeros(n)
    d = np.zeros(n)
    c[n-1] = z[n-1]
    b[n-1] = (a[n] - a[n-1]) / h[n-1] - (h[n-1] / 3) * (2 * c[n-1])
    d[n-1] = (-c[n-1]) / (3 * h[n-1])

    for i in range(n - 2, -1, -1):
        c[i] = z[i] - r[i] * c[i + 1]
        b[i] = (a[i + 1] - a[i]) / h[i] - (h[i] / 3) * (c[i + 1] + 2 * c[i])
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])

    return a, b, c, d


def main():
    n = 3
    x = np.array([0, 1, 2, 3])
    y = np.array([1, e, e ** 2, e ** 3])
    result = cubic_spline_natural(n, x, y)

    for i in range(n):
        for j in range(4):
            print(result[j][i], end=' ')
        print()


if __name__ == '__main__':
    main()
