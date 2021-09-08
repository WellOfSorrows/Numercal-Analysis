import numpy as np
from numpy import linalg as la


def gaussian_elimination_partial_pivoting(dimensions, matrix: np.array):
    n = dimensions
    a = matrix

    #   Initialization
    n_row = np.array([i for i in range(n)])

    #   Elimination
    for i in range(n-1):
        maximum = 0
        for j in range(i, n):
            temp = abs(a[i][j])
            if temp > maximum:
                maximum = temp
        for p in range(i, n, 1):
            if a[n_row[p]][i] == maximum:
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


def iterative_refinement(dimensions, matrix: np.array, ans_vector: np.array, initial_guess: np.array, precision,
                         tolerance=10**(-5), max_iterations=1000):
    n = dimensions
    a = matrix
    b = ans_vector
    xo = initial_guess
    t = precision
    tol = tolerance
    n_0 = max_iterations

    x = gaussian_elimination_partial_pivoting(n, a)


