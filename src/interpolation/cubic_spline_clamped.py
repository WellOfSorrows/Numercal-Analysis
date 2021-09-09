import numpy as np
from math import e


def cubic_spline_clamped(number_of_splines, x_values: np.array, y_values: np.array,
                         left_endpoint_derivative, right_endpoint_derivative):
    """
    :return: The clamped cubic spline coefficients.
    """

    n = number_of_splines
    x = x_values
    a = y_values
    fpo = left_endpoint_derivative
    fpn = right_endpoint_derivative

    if len(x) != len(a):
        print("The vectors x_values & y_values must be of the same length.")
        return None

    h = np.zeros(n)
    for i in range(n):
        h[i] = x[i + 1] - x[i]

    alpha = np.zeros(n + 1)
    alpha[0] = (3 / h[0]) * (a[1] - a[0]) - 3 * fpo
    alpha[n] = 3 * fpn - (3 / h[n - 1]) * (a[n] - a[n - 1])
    for i in range(1, n):
        alpha[i] = (3 / h[i]) * (a[i + 1] - a[i]) - (3 / h[i - 1]) * (a[i] - a[i - 1])

    p = np.zeros(n + 1)
    r = np.zeros(n + 1)
    z = np.zeros(n + 1)
    p[0] = 2 * h[0]
    r[0] = 0.5
    z[0] = alpha[0] / p[0]

    for i in range(1, n):
        p[i] = 2 * (x[i + 1] - x[i - 1]) - (h[i - 1] * r[i - 1])
        r[i] = h[i] / p[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / p[i]

    p[n] = h[n - 1] * (2 - r[n - 1])
    z[n] = (alpha[n] - h[n - 1] * z[n - 1]) / p[n]

    c = np.zeros(n)
    b = np.zeros(n)
    d = np.zeros(n)
    c[n-1] = z[n-1] - r[n-1] * z[n]
    b[n-1] = (a[n] - a[n-1]) / h[n-1] - (h[n-1] / 3) * (z[n] + 2 * c[n-1])
    d[n-1] = (z[n] - c[n-1]) / (3 * h[n-1])

    for i in range(n - 2, -1, -1):
        c[i] = z[i] - r[i] * c[i + 1]
        b[i] = (a[i + 1] - a[i]) / h[i] - (h[i] / 3) * (c[i + 1] + 2 * c[i])
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])

    return a, b, c, d
