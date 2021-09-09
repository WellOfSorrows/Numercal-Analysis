from math import log
from src.root_finding.bisection_method import bisection_method


def f(x):
    return x**2 - 4 * x + 4 - log(x)


def main():
    left_endpoint = 2
    right_endpoint = 4
    result = bisection_method(f, left_endpoint, right_endpoint)
    print("The result obtained from bisection method is: {result}".format(result=result))


if __name__ == '__main__':
    main()
