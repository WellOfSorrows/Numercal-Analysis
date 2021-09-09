import numpy as np


def bezier_curve(number, points: np.array, left_guide_points: np.array, right_guide_points: np.array):
    """
    :return: Alpha and beta coefficients of Bezier's cubic curve.
    """

    n = number
    x = np.array([points[i][0] for i in range(n+1)])
    y = np.array([points[i][1] for i in range(n+1)])

    x_plus = np.zeros(n + 1)
    y_plus = np.zeros(n + 1)
    for i in range(n):
        x_plus[i] = left_guide_points[i][0]
        y_plus[i] = left_guide_points[i][1]

    x_minus = np.zeros(n + 1)
    y_minus = np.zeros(n + 1)
    for i in range(1, n + 1):
        x_minus[i] = right_guide_points[i - 1][0]
        y_minus[i] = right_guide_points[i - 1][1]

    a = np.zeros((n, 4))
    b = np.zeros((n, 4))
    for i in range(n):
        a[i][0] = x[i]
        b[i][0] = y[i]
        a[i][1] = 3 * (x_plus[i] - x[i])
        b[i][1] = 3 * (y_plus[i] - y[i])
        a[i][2] = 3 * (x[i] + x_minus[i + 1] - 2 * x_plus[i])
        b[i][2] = 3 * (y[i] + y_minus[i + 1] - 2 * y_plus[i])
        a[i][3] = x[i + 1] - x[i] + 3 * x_plus[i] - 3 * x_minus[i + 1]
        b[i][3] = y[i + 1] - y[i] + 3 * y_plus[i] - 3 * y_minus[i + 1]

    return a, b
