import numpy as np


def bezier_curve(number,
                 points: np.array,
                 x_left_guide_points: np.array, y_left_guide_points: np.array,
                 x_right_guide_points: np.array, y_right_guide_points: np.array):
    n = number
    x = np.array([points[i][0] for i in range(n+1)])
    y = np.array([points[i][1] for i in range(n+1)])

    x_plus = np.zeros(n + 1)
    for i in range(n):
        x_plus[i] = x_left_guide_points[i]

    y_plus = np.zeros(n + 1)
    for i in range(n):
        y_plus[i] = y_left_guide_points[i]

    x_minus = np.zeros(n + 1)
    for i in range(1, n + 1):
        x_minus[i] = x_right_guide_points[i - 1]

    y_minus = np.zeros(n + 1)
    for i in range(1, n + 1):
        y_minus[i] = y_right_guide_points[i - 1]

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


def main():
    n = 4
    x = np.array([(3,6), (2,2,) 6, 5, 6.5])
    y = np.array([6, 2, 6, 2, 3])
    x_plus = np.array([3.3, 2.8, 5.8, 5.5])
    y_plus = np.array([6.5, 3, 5, 2.2])
    x_minus = np.array([2.5, 5, 4.5, 6.4])
    y_minus = np.array([2.5, 5.8, 2.5, 2.8])

    result = bezier_curve(n, x, y, x_plus, y_plus,
                          x_minus, y_minus)
    print(result[0])
    print(result[1])


if __name__ == '__main__':
    main()
