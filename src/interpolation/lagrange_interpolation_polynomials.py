import numpy as np


def lagrange_interpolation(point_to_eval, x_values: np.array, y_values: np.array):
    """
    It is suggested to use other interpolation methods than this one.
    :return: The interpolated value at the given point.
    """
    z = point_to_eval
    x = x_values
    y = y_values

    if len(x) != len(y):
        print("The vectors x_values & y_values must be of the same length.")
        return None

    p = 0
    n = len(x)
    w = np.ones(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                w[i] = (z - x[j])/(x[i] - x[j])*w[i]
        p += w[i] * y[i]

    return p


def main():
    z = 1.5
    x = np.array([1, 1.3, 1.6, 1.9, 2.2])
    y = np.array([0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623])

    res = lagrange_interpolation(z, x, y)
    print(res)


if __name__ == '__main__':
    main()

