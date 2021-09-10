import numpy as np
from src.linear_direct_methods.ldlt_factorization import ldlt_factorization


def main():
    n = 3
    matrix = np.array([[4, -1, 1],
                       [-1, 4.25, 2.75],
                       [1, 2.75, 3.5]])
    result = ldlt_factorization(n, matrix)
    print("The lower-triangular matrix: \n{res}".format(res=result[0]),
          "\n\nThe diagonal matrix: \n{res}".format(res=result[1]))


if __name__ == '__main__':
    main()
