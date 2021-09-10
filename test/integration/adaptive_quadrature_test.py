from math import sin
from src.integration.adaptive_quadrature import adaptive_quadrature


def g(x):
    return (100 / (x**2)) * sin(10 / x)


def main():
    result = adaptive_quadrature(g, 1, 3, 10**(-4))
    print("The value obtained by adaptive quadrature within given precision is: {res}".format(res=result))


if __name__ == '__main__':
    main()
