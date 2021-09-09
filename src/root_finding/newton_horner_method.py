import numpy as np


def horner_method(degree, coefficients: np.array, point):
    """
    :return: The value of the polynomial and the derivative of the polynomial at the given point.
    """
    n = degree
    a = coefficients
    x_0 = point

    y = a[0]
    z = a[0]

    for i in range(1, n):
        y = x_0 * y + a[i]
        z = x_0 * z + y

    y = x_0 * y + a[n]
    return y, z


def newton_horner_method(degree, coefficients: np.array, initial_approximation,
                         tolerance=10**(-5), max_iterations=200):
    """
    :return: The approximate root within the given tolerance, or a message that the operation has failed.
    """

    n = degree
    a = coefficients
    p_0 = initial_approximation
    tol = tolerance
    n_0 = max_iterations

    i = 0
    while i < n_0:
        y, z = horner_method(n, a, p_0)
        if z == 0:
            print("Divide by zero detected.")
            return None
        p = p_0 - y/z
        if abs(p - p_0) < tol:
            return p
        p_0 = p
        i += 1

    print("Max number of iterations exceeded.")
    return None


def main():
    degree = 4
    coefficients = np.array([2, 0, -3, 3, -4])
    initial_approximation = -2
    result = newton_horner_method(degree, coefficients, initial_approximation)
    print(result)


if __name__ == '__main__':
    main()
