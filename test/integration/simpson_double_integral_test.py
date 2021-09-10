from math import exp
from src.integration.simpson_double_integral import simpson_double_integral


def f(x, y):
    return exp(y/x)


def d(x):
    return x**2


def c(x):
    return x**3


def main():
    result = simpson_double_integral(f, c, d, 0.1, 0.5, 10, 10)
    print("The approximated value of the integral using Simpson's double integration is: {res}".format(res=result))


if __name__ == '__main__':
    main()
