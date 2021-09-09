import numpy as np


def neville_iterated_interpolation(point_to_eval, x_values: np.array, y_values: np.array):
    """
    :return: The complete interpolation table.
    """

    z = point_to_eval
    x = x_values
    y = y_values

    if len(x) != len(y):
        print("The vectors x_values & y_values must be of the same length.")
        return None

    n = len(x)
    q = np.zeros((n, n))
    for i in range(n):
        q[i][0] = y[i]

    for i in range(1, n):
        for j in range(1, i+1):
            q[i][j] = ((z - x[i-j]) * q[i][j-1] - (z - x[i]) * q[i-1][j-1]) / (x[i] - x[i-j])

    return q


def main():
    z = 1.5
    x = np.array([1, 1.3, 1.6, 1.9, 2.2])
    y = np.array([0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623])

    res = neville_iterated_interpolation(z, x, y)
    print(res)


if __name__ == '__main__':
    main()
