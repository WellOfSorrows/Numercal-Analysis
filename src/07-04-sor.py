import numpy as np
from numpy import linalg as la


def sor(dimensions, matrix: np.array, ans_vector: np.array, initial_guess: np.array, parameter,
        tolerance=10**(-5), max_iterations=1000):
    n = dimensions
    a = matrix
    b = ans_vector
    xo = initial_guess
    w = parameter
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
            x[i] = (1 - w) * xo[i] + (w * (b[i] - sum_of_0 - sum_of_1)) / a[i][i]

        diff = np.array(x - xo)
        err = la.norm(diff)
        if err < tol:
            return x

        k += 1
        xo = np.array(x)

    print("Max number of iterations exceeded.")
    return None


def main():
    n = 3
    mat = np.array([[4, 3, 0],
                    [3, 4, -1],
                    [0, -1, 4]])

    ans = np.array([24, 30, -24])
    init = np.ones(n)

    result = sor(n, mat, ans, init, 1.25)
    print(result)


if __name__ == '__main__':
    main()
