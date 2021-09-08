import numpy as np


def neville_iterated_interpolation(point_to_eval, x_values: np.array, y_values: np.array):
    z = point_to_eval
    x = x_values
    y = y_values

    n = len(x)
    q = np.zeros(n)
    for i in range(n):
        for j in range(n - i):
            if i == 0:
                q[j] = y[j]
            else:
                q[j] = ((z - x[j + i]) * q[j] + (x[j] - z) * q[j + 1]) / (x[j] - x[j + i])

    return q[0]


def main():
    z = 1.5
    x = np.array([1, 1.3, 1.6, 1.9, 2.2])
    y = np.array([0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623])

    res = neville_iterated_interpolation(z, x, y)
    print(res)


if __name__ == '__main__':
    main()
