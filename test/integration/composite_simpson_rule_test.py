from src.integration.composite_simpson_rule import composite_simpson_rule


def f(x):
    return x ** 2


def main():
    result = composite_simpson_rule(f, 0, 3.5)
    print("The approximated value of the integral using composite Simpson's rule is: {res}".format(res=result))


if __name__ == '__main__':
    main()
