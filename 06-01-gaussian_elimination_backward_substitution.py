import numpy as np


def gaussian_elimination_backward_substitution(dimensions, matrix: np.array):
    n = dimensions
    a = matrix

    #   Gaussian Elimination
    for i in range(n-1):
        p = -1
        flag = False
        for j in range(i, n, 1):
            if a[j][i] != 0:
                flag = True
                p = j
                break

        if flag is False:
            print('No unique solution exists')
            return None

        if p != i:
            a[p], a[i] = a[i], a[p]
        for j in range(i+1, n, 1):
            m = a[j][i] / a[i][i]
            a[j] = np.array(a[j] - m * a[i])

    if a[n-1][n-1] == 0:
        print('No unique solution exists')
        return None

    #   Backward substitution
    x = np.zeros(n)
    x[n-1] = a[n-1][n] / a[n-1][n-1]
    for i in range(n-2, -1, -1):
        sum_of = 0
        for j in range(i+1, n):
            sum_of += a[i][j] * x[j]
        x[i] = (a[i][n] - sum_of) / a[i][i]
    return x

