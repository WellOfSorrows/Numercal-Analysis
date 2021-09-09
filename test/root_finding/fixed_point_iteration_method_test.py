from src.root_finding.fixed_point_iteration_method import fixed_point_iteration_method


def g(x):
    return (3*x**4 + 2*x**2 + 3) / (4*x**3 + 4*x - 1)


def main():
    a = 1
    result = fixed_point_iteration_method(g, a)
    print("The result obtained by the fixed-point iteration method is: {result}".format(result=result))


if __name__ == '__main__':
    main()
