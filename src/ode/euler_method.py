def euler_method_ode(function, left_endpoint, right_endpoint, number, initial_value):
    f = function
    a = left_endpoint
    b = right_endpoint
    n = number
    w = initial_value

    h = (b-a)/n
    t = a

    for i in range(1, n+1, 1):
        w = w + h * f(t, w)
        t = a + i*h

    return t, w
