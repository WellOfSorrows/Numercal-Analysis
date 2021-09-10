from math import sin
from src.ode.euler_method import euler_method


def f(t, y):
    return t**(-2) * (sin(2*t) - 2*t*y)


def main():
    a = 1
    b = 2
    n = 4
    initial = 2
    result = euler_method(f, a, b, n, initial)
    print("The value obtained from Euler's method is: {res}".format(res=result[1]))


if __name__ == '__main__':
    main()
