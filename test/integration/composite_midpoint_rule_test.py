from math import sin, pi
from src.integration.composite_midpoint_rule import composite_midpoint_rule


def f(x):
    return x * sin(x)


def main():
    result = composite_midpoint_rule(f, 0, pi/2)
    print("The approximated value of the integral using midpoint is: {res}".format(res=result))


if __name__ == '__main__':
    main()
