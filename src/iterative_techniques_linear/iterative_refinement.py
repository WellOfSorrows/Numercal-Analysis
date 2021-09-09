import numpy as np
from numpy import linalg as la
from src.direct_methods_linear.gaussian_elimination_partial_pivoting import gaussian_elimination_partial_pivoting


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


