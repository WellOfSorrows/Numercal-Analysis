from src.root_finding.muller_method import muller_method


def f(x):
    return x**4 - 3 * x**3 + x**2 + x + 1


def main():
    a = 0.5
    b = -0.5
    c = 0
    result = muller_method(f, a, b, c)
    print("The result obtained by the muller method is: {result}".format(result=result))


if __name__ == '__main__':
    main()
