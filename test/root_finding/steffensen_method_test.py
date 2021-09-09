from src.root_finding.steffensen_method import steffensen_method
from math import sqrt


def g(x):
    return sqrt(10 / (x + 4))


def main():
    a = 1.5
    result = steffensen_method(g, a)
    print("The result obtained by the Steffensen's method is: {result}".format(result=result))


if __name__ == '__main__':
    main()
