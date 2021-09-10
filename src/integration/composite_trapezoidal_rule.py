import numpy as np


def composite_trapezoidal_rule(function, left_endpoint, right_endpoint, length=50):
    f = function
    a = left_endpoint
    b = right_endpoint
    n = length

    h = (b - a) / n
    xi = np.array([f(a) + f(b), 0])

    for i in range(1, n):
        xi[1] += f(a + i * h)

    s = (h / 2) * (xi[0] + 2 * xi[1])
    return s
