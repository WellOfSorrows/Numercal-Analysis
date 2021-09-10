import numpy as np


def adaptive_quadrature(function, left_endpoint, right_endpoint,
                        tolerance=10**(-5), number_of_levels=10):
    f = function
    a = left_endpoint
    b = right_endpoint
    tol = tolerance
    n = number_of_levels

    diffs = np.zeros(n)
    p = np.zeros(n)
    h = np.zeros(n)
    fa = np.zeros(n)
    fb = np.zeros(n)
    fc = np.zeros(n)
    s = np.zeros(n)
    v = np.zeros(8)
    m = np.zeros(n)

    app = 0
    diffs[0] = 10 * tol
    p[0] = a
    h[0] = (b-a) / 2
    fa[0] = f(a)
    fb[0] = f(b)
    fc[0] = f(a + h[0])
    s[0] = h[0] * (fa[0] + 4 * fc[0] + fb[0])/3
    m[0] = 1

    i = 0
    while i >= 0:
        fd = f(p[i] + h[i]/2)
        fe = f(p[i] + 3*h[i]/2)

        s_1 = h[i] * (fa[i] + 4 * fd + fc[i])/6
        s_2 = h[i] * (fc[i] + 4 * fe + fb[i])/6
        v[0] = p[i]
        v[1] = fa[i]
        v[2] = fc[i]
        v[3] = fb[i]
        v[4] = h[i]
        v[5] = diffs[i]
        v[6] = s[i]
        v[7] = m[i]

        i -= 1
        if abs(s_1 + s_2 - v[6]) < v[5]:
            app += (s_1 + s_2)
        else:
            if v[7] > n:
                print("Level exceeded.")
                return None

            i += 1
            p[i] = v[0] + v[4]
            fa[i] = v[2]
            fc[i] = fe
            fb[i] = v[3]
            h[i] = v[4]/2
            diffs[i] = v[5]/2
            s[i] = s_2
            m[i] = v[7] + 1

            i += 1
            p[i] = v[0]
            fa[i] = v[1]
            fc[i] = fd
            fb[i] = v[2]
            h[i] = h[i-1]
            diffs[i] = diffs[i-1]
            s[i] = s_1
            m[i] = m[i-1]

    return app
