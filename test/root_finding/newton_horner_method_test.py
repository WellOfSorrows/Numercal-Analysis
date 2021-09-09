import numpy as np
from src.root_finding.newton_horner_method import newton_horner_method


def main():
    n = 4
    coeffs = np.array([2, 0, -3, 3, -4])
    x_0 = -2
    result = newton_horner_method(n, coeffs, x_0)
    print("The result obtained by the Newton-Horner method is: {result}".format(result=result))


if __name__ == '__main__':
    main()
