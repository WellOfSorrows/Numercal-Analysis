def secant_method(function, first_initial_approximation, second_initial_approximation,
                  tolerance=10**(-5), max_iterations=200):
    """
    :return: The approximate root within the given tolerance, or a message that the operation has failed.
    """

    f = function
    p_0 = first_initial_approximation
    p_1 = second_initial_approximation
    tol = tolerance
    n_0 = max_iterations

    q_0 = f(p_0)
    q_1 = f(p_1)

    i = 1
    while i < n_0:
        p = p_1 - q_1 * (p_1 - p_0)/(q_1 - q_0)
        if abs(p - p_1) < tol:
            return p
        p_0, q_0 = p_1, q_1
        p_1, q_1 = p, f(p)
        i += 1

    print("Max number of iterations exceeded.")
    return None
