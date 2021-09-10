def runge_kutta_method(function, left_endpoint, right_endpoint, number, initial_value):
    """
    Note this is the Runge-Kutta method of order four.
    """

    f = function
    a = left_endpoint
    b = right_endpoint
    n = number
    w = initial_value

    h = (b - a) / n
    t = a

    for i in range(1, n + 1, 1):
        k_1 = h * f(t, w)
        k_2 = h * f(t + h/2, w + k_1/2)
        k_3 = h * f(t + h/2, w + k_2/2)
        k_4 = h * f(t + h, w + k_3)

        w = w + (k_1 + 2*k_2 + 2*k_3 + k_4) / 6
        t = a + i*h

    return t, w
