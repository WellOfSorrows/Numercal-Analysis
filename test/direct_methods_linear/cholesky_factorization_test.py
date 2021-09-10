import numpy as np
from src.direct_methods_linear.cholesky_factorization import cholesky_factorization


def main():
    dimensions = 3
    matrix = np.array([[4, -1, 1],
                       [-1, 4.25, 2.75],
                       [1, 2.75, 3.5]])
    result = cholesky_factorization(dimensions, matrix)
    print("The lower-triangular matrix obtained from Cholesky's factorization is: \n{res}".format(res=result))


if __name__ == '__main__':
    main()
