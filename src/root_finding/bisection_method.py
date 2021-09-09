def bisection_method(function, left_endpoint, right_endpoint,
                     tolerance=10**(-5), max_iterations=200):
    """
    :return: The approximate root within the given tolerance, or a message that the operation has failed.
    """

    f = function
    a = left_endpoint
    b = right_endpoint
    tol = tolerance
    n_0 = max_iterations

    fa = f(a)

    i = 0
    while i < n_0:
        p = a + (b - a)/2
        fp = f(p)
        if fp == 0 or (b - a)/2 < tol:
            return p
        if fa * fp > 0:
            a = p
            fa = fp
        else:
            b = p
        i += 1

    print("Max number of iterations exceeded.")
    return None
