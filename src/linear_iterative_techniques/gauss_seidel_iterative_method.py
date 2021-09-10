import numpy as np
from numpy import linalg as la


def gauss_seidel_iterative_method(dimensions, matrix: np.array, ans_vector: np.array, initial_guess: np.array,
                                  tolerance=10**(-5), max_iterations=1000):
    n = dimensions
    a = matrix
    b = ans_vector
    xo = initial_guess
    tol = tolerance
    n_0 = max_iterations

    x = np.zeros(n)

    k = 0
    while k < n_0:
        for i in range(n):
            sum_of_0 = 0
            sum_of_1 = 0
            for j in range(i):
                sum_of_0 += (a[i][j] * x[j])
            for j in range(i+1, n, 1):
                sum_of_1 += (a[i][j] * xo[j])
            x[i] = (b[i] - sum_of_0 - sum_of_1) / (a[i][i])

        diff = np.array(x - xo)
        err = la.norm(diff)
        if err < tol:
            return x

        k += 1
        xo = np.array(x)

    print("Max number of iterations exceeded.")
    return None

