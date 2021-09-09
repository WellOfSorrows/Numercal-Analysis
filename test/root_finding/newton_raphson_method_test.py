from src.root_finding.newton_raphson_method import newton_raphson_method
from math import cos, sin, pi


def f(x):
    return cos(x) - x


def df(x):
    return -sin(x) - 1


def main():
    a = pi/4
    result = newton_raphson_method(f, df, a)
    print("The result obtained by the Newton-Raphson method is: {result}".format(result=result))


if __name__ == '__main__':
    main()
