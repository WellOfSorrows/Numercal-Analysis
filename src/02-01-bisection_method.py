def bisection_method(function, left_endpoint, right_endpoint,
                     tolerance=10**(-5), max_iterations=1000):
    f = function
    a = left_endpoint
    b = right_endpoint
    tol = tolerance
    n_0 = max_iterations

    i = 0
    fa = f(a)
    while i < n_0:
        p = a + (b-a)/2
        fp = f(p)
        if fp == 0 or (b-a)/2 < tol:
            return p
        i += 1
        if fa * fp > 0:
            a = p
            fa = fp
        else:
            b = p

    print("Max number of iterations exceeded.")
    return None
