from src.root_finding.bisection_method import bisection_method


def f(x):
    return x**2 - 3


def main():
    a = 0
    b = 2
    tol = 10**(-6)
    max_iterations = 100
    result = bisection_method(f, a, b, tolerance=tol, max_iterations=max_iterations)
    print("The result obtained by the bisection method is: {result}".format(result=result))


if __name__ == '__main__':
    main()
