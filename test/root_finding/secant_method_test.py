from src.root_finding.secant_method import secant_method
from math import exp


def f(x):
    return exp(x) - 3 * x ** 2


def main():
    a = 0
    b = 1
    result = secant_method(f, a, b)
    print("The result obtained by the secant method is: {result}".format(result=result))


if __name__ == '__main__':
    main()
