import numpy as np
from src.interpolation.cubic_spline_natural import cubic_spline_natural
from math import e


def main():
    n = 3
    x = np.array([0, 1, 2, 3])
    y = np.array([1, e, e ** 2, e ** 3])
    result = cubic_spline_natural(n, x, y)

    for i in range(n):
        print("The coefficients of the natural cubic spline #{index} are: ".format(index=i+1))
        for j in range(4):
            print("\t{res}".format(res=result[j][i], end=' '))
        print()


if __name__ == '__main__':
    main()
