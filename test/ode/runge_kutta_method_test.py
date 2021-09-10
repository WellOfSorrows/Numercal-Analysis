from math import sin
from src.ode.runge_kutta_method import runge_kutta_method


def f(t, y):
    return t**(-2) * (sin(2*t) - 2*t*y)


def main():
    a = 1
    b = 2
    n = 4
    initial = 2
    result = runge_kutta_method(f, a, b, n, initial)
    print("The value obtained from Runge-Kutta order four method is: {res}".format(res=result[1]))


if __name__ == '__main__':
    main()
