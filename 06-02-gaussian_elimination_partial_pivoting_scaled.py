import numpy as np


def gaussian_elimination_partial_pivoting_scaled(dimensions, matrix: np.array):
    n = dimensions
    a = matrix

    #   Initialization
    s = np.zeros(n)
    n_row = np.zeros(n, dtype=int)

    for i in range(n):
        maximum = 0
        for j in range(n):
            temp = abs(a[i][j])
            if temp > maximum:
                maximum = temp
        s[i] = maximum
        if s[i] == 0:
            print('No unique solution exists')
            return None
        else:
            n_row[i] = i

    #   Elimination
    for i in range(n-1):
        maximum = 0
        for j in range(i, n):
            temp = abs(a[n_row[j]][i] / s[n_row[j]])
            if temp > maximum:
                maximum = temp
        for p in range(i, n, 1):
            if abs(a[n_row[p]][i]) / s[n_row[p]] == maximum:
                break

        if a[n_row[p]][i] == 0:
            print('No unique solution exists')
            return None

        if n_row[i] != n_row[p]:
            n_row[i], n_row[p] = n_row[p], n_row[i]
        for j in range(i+1, n, 1):
            m = a[n_row[j]][i] / a[n_row[i]][i]
            a[n_row[j]] = np.array(a[n_row[j]] - m * a[n_row[i]])

    if a[n_row[n-1]][n-1] == 0:
        print('No unique solution exists')
        return None

    #   Backward substitution
    x = np.zeros(n)
    x[n-1] = a[n_row[n-1]][n] / a[n_row[n-1]][n-1]
    for i in range(n-2, -1, -1):
        sum_of = 0
        for j in range(i+1, n):
            sum_of += a[n_row[i]][j] * x[j]
        x[i] = (a[n_row[i]][n] - sum_of) / a[n_row[i]][i]
    return x


def main():
    dimensions = 3
    matrix = np.array([[2.11, -4.21, 0.921, 2.01],
                       [4.01, 10.2, -1.12, -3.09],
                       [1.09, 0.987, 0.832, 4.21]])

    dimensions = 2
    matrix = np.array([[30, 591400, 591700], [5.291, -6.13, 46.78]])
    res = gaussian_elimination_partial_pivoting_scaled(dimensions, matrix)
    print(res[0], res[1])


if __name__ == '__main__':
    main()
