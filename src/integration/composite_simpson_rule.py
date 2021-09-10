import numpy as np


def composite_simpson_rule(function, left_endpoint, right_endpoint, length=8):
    f = function
    a = left_endpoint
    b = right_endpoint
    n = length

    h = (b - a) / n
    xi = np.zeros(3)
    xi[0] = f(a) + f(b)

    for i in range(1, n):
        if i % 2 == 0:
            xi[2] = xi[2] + f(a + i * h)
        else:
            xi[1] = xi[1] + f(a + i * h)

    s = (h / 3) * (xi[0] + 4 * xi[1] + 2 * xi[2])
    return s
