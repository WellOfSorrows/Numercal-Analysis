from math import sin, pi, e

from src.integration.romberg_integration import romberg_integration


def g(x):
    return (e**(3*x)) * sin(2*x)


def main():
    n = 10
    result = romberg_integration(g, 0, pi/4, n)
    print("The approximated value of the integral using Romberg's integration is: {res}".format(res=result))


if __name__ == '__main__':
    main()
