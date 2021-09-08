def secant_method(function, first_initial_approximation, second_initial_approximation,
                  tolerance=10**(-5), max_iterations=1000):
    f = function
    p_0 = first_initial_approximation
    p_1 = second_initial_approximation
    tol = tolerance
    n_0 = max_iterations

    i = 1
    q_0 = f(p_0)
    q_1 = f(p_1)

    while i < n_0:
        p = p_1 - q_1 * (p_1 - p_0)/(q_1 - q_0)
        if abs(p - p_1) < tol:
            return p
        i += 1
        p_0 = p_1
        q_0 = q_1
        p_1 = p
        q_1 = f(p)

    print("Max number of iterations exceeded.")
    return None

