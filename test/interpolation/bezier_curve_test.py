import numpy as np
from src.interpolation.bezier_curve import bezier_curve


def main():
    n = 4
    p = np.array([(3, 6), (2, 2), (6, 6), (5, 2), (6.5, 3)])
    p_plus = np.array([(3.3, 6.5), (2.8, 3), (5.8, 5), (5.5, 2.2)])
    p_minus = np.array([(2.5, 2.5), (5, 5.8), (4.5, 2.5), (6.4, 2.8)])

    result = bezier_curve(n, p, p_plus, p_minus)
    print("The alpha coefficients of Bezier's curve: \n{res}".format(res=result[0]))
    print()
    print("The beta coefficients of Bezier's curve: \n{res}".format(res=result[1]))


if __name__ == '__main__':
    main()
