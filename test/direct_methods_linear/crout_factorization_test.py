import numpy as np
from src.direct_methods_linear.crout_factorization import crout_factorization


def main():
    n = 4
    a = np.array([[2, -1, 0, 0, 1],
                  [-1, 2, -1, 0, 0],
                  [0, -1, 2, -1, 0],
                  [0, 0, -1, 2, 1]])
    result = crout_factorization(n, a)
    print("The solutions obtained from Crout factorization are: {res}".format(res=result))


if __name__ == '__main__':
    main()
