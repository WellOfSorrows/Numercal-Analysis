def fixed_point_iteration_method(function, initial_approximation,
                                 tolerance=10**(-5), max_iterations=1000):
    g = function
    p_0 = initial_approximation
    tol = tolerance
    n_0 = max_iterations

    i = 0
    while i < n_0:
        p = g(p_0)
        if abs(p - p_0) < tol:
            return p
        i += 1
        p_0 = p

    print("Max number of iterations exceeded.")
    return None

