import numpy as np
from src.interpolation.hermite_interpolation import hermite_interpolation


def main():
    x = np.array([1.3, 1.6, 1.9])
    y = np.array([0.6200860, 0.4554022, 0.2818186])
    dy = np.array([-0.5220232, -0.5698959, -0.5811571])
    result = hermite_interpolation(x, y, dy)
    print("The Hermite coefficients are:\n\t{res}".format(res=result))


if __name__ == '__main__':
    main()
