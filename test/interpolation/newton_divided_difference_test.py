import numpy as np
from src.interpolation.newton_divided_difference import newton_divided_difference


def main():
    x = np.array([1, 1.3, 1.6, 1.9, 2.2])
    y = np.array([0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623])
    result = newton_divided_difference(x, y)
    print("The Newton's divided difference table is: \n{res}".format(res=result))


if __name__ == '__main__':
    main()
