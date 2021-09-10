import numpy as np
from src.direct_methods_linear.gaussian_elimination_backward_substitution import \
    gaussian_elimination_backward_substitution


def main():
    dimensions = 2
    matrix = np.array([[30, 591400, 591700], [5.291, -6.13, 46.78]])
    result = gaussian_elimination_backward_substitution(dimensions, matrix)
    print("The solutions obtained from Gaussian elimination with backward substitution are: {res}".format(res=result))


if __name__ == '__main__':
    main()
