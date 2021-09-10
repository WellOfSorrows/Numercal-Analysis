import numpy as np
from src.linear_direct_methods.gaussian_elimination_partial_pivoting import gaussian_elimination_partial_pivoting


def main():
    dimensions = 2
    matrix = np.array([[30, 591400, 591700], [5.291, -6.13, 46.78]])
    result = gaussian_elimination_partial_pivoting(dimensions, matrix)
    print("The solutions obtained from Gaussian elimination with partial pivoting are: {res}".format(res=result))


if __name__ == '__main__':
    main()
