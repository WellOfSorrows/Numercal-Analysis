import numpy as np


def gaussian_double_integral(function,
                             left_endpoint_function, right_endpoint_function,
                             left_endpoint, right_endpoint,
                             legendre_roots: np.array, legendre_coefficients: np.array,
                             first_length=5, second_length=5):
    f = function
    a = left_endpoint
    b = right_endpoint
    c = left_endpoint_function
    d = right_endpoint_function
    r = legendre_roots
    coeffs = legendre_coefficients
    n = first_length
    m = second_length

    h_1 = (b-a)/2
    h_2 = (b+a)/2
    s = 0

    for i in range(m):
        jx = 0
        x = h_1 * r[m][i] + h_2
        d_1 = d(x)
        c_1 = c(x)
        k_1 = (d_1 - c_1)/2
        k_2 = (d_1 + d_1)/2
        for j in range(n):
            y = k_1 * r[n][j] + k_2
            q = f(x, y)
            jx += coeffs[n][j] * q
        s += coeffs[m][i] * k_1 * jx
    s = h_1 * s
    return s
