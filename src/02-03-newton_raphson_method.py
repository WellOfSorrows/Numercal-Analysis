def newton_raphson_method(function, derivative, initial_approximation,
                          tolerance=10**(-5), max_iterations=1000):
    f = function
    df = derivative
    p_0 = initial_approximation
    tol = tolerance
    n_0 = max_iterations

    i = 0
    while i < n_0:
        if df(p_0) == 0:
            print("Divide by zero detected.")
            return None
        p = p_0 - f(p_0)/df(p_0)
        if abs(p - p_0) < tol:
            return p
        i += 1
        p_0 = p

    print("Max number of iterations exceeded.")
    return None
