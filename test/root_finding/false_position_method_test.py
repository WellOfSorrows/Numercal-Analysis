from math import cos, pi
from src.root_finding.false_position_method import false_position_method


def f(x):
    return x - cos(x)


def main():
    a = 0.5
    b = pi/4
    result = false_position_method(f, a, b)
    print("The result obtained by the false position method is: {result}".format(result=result))


if __name__ == '__main__':
    main()
