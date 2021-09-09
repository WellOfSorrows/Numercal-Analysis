import numpy as np
from src.interpolation.lagrange_interpolation_polynomials import lagrange_interpolation


def main():
    z = 1.5
    x = np.array([1, 1.3, 1.6, 1.9, 2.2])
    y = np.array([0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623])

    result = lagrange_interpolation(z, x, y)
    print("The value obtained from Lagrange interpolation is: {res}".format(res=result))


if __name__ == '__main__':
    main()
