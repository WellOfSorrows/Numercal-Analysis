from cmath import sqrt


def muller_method(function, first_initial_approximation, second_initial_approximation, third_initial_approximation,
                  tolerance=10**(-5), max_iterations=200):
    """
    :return: The approximate root within the given tolerance, or a message that the operation has failed.
             Note that Muller's method returns complex-valued roots.
    """

    f = function
    p_0 = first_initial_approximation
    p_1 = second_initial_approximation
    p_2 = third_initial_approximation
    tol = tolerance
    n_0 = max_iterations

    h_1 = p_1 - p_0
    h_2 = p_2 - p_1
    s_1 = (f(p_1) - f(p_0))/h_1
    s_2 = (f(p_2) - f(p_1))/h_2
    d_1 = (s_2 - s_1)/(h_2 + h_1)

    i = 2
    while i < n_0:
        b = s_2 + h_2 * d_1
        d_2 = sqrt(b**2 - 4 * f(p_2) * d_1)

        if abs(b - d_2) < abs(b + d_2):
            e = b + d_2
        else:
            e = b - d_2

        h = -2 * f(p_2) / e
        p = p_2 + h
        if abs(h) < tol:
            return p

        p_0, p_1, p_2 = p_1, p_2, p
        h_1, h_2 = p_1 - p_0, p_2 - p_1
        s_1, s_2 = (f(p_1) - f(p_0))/h_1, (f(p_2) - f(p_1))/h_2
        d_1 = (s_2 - s_1)/(h_2 + h_1)
        i += 1

    print("Max number of iterations exceeded.")
    return None
