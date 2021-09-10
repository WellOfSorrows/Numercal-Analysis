from src.integration.composite_trapezoidal_rule import composite_trapezoidal_rule


def f(x):
    return 1 / x


def main():
    result = composite_trapezoidal_rule(f, 1, 2, length=4)
    print("The approximated value of the integral using the trapezoidal rule is: {res}".format(res=result))


if __name__ == '__main__':
    main()
