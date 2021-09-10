import numpy as np


def simpson_double_integral(function,
                            left_endpoint_function, right_endpoint_function,
                            left_endpoint_constant, right_endpoint_constant,
                            first_length=50, second_length=50):
    f = function
    a = left_endpoint_constant
    b = right_endpoint_constant
    c = left_endpoint_function
    d = right_endpoint_function
    n = first_length
    m = second_length

    h = (b - a) / n
    p = np.zeros(3)

    for i in range(n+1):
        x = a + i * h
        hx = (d(x) - c(x)) / m
        k = np.zeros(3)
        k[0] = f(x, c(x)) + f(x, d(x))
        for j in range(1, m):
            y = c(x) + j * hx
            q = f(x, y)
            if j % 2 == 0:
                k[1] += q
            else:
                k[2] += q
        L = (k[0] + 2 * k[1] + 4 * k[2]) * hx / 3

        if i == 0 or i == n:
            p[0] += L
        else:
            if i % 2 == 0:
                p[1] += L
            else:
                p[2] += L
    s = h * (p[0] + 2 * p[1] + 4 * p[2]) / 3
    return s
