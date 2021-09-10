import numpy as np


def composite_midpoint_rule(function, left_endpoint, right_endpoint, length=50):
    f = function
    a = left_endpoint
    b = right_endpoint
    n = length

    h = (b - a) / (n + 2)
    xi = 0

    x = np.zeros(n + 2)
    x[0] = a
    for i in range(n + 2):
        x[i] = (a + (i + 1) * h)

    for i in range(int(n / 2)):
        xi += f(x[2 * i])

    s = 2 * h * xi
    return s
