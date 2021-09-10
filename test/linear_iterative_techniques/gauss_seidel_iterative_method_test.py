import numpy as np
from src.linear_iterative_techniques.gauss_seidel_iterative_method import gauss_seidel_iterative_method


def main():
    n = 4
    mat = np.array([[10, -1, 2, 0],
                    [-1, 11, -1, 3],
                    [2, -1, 10, -1],
                    [0, 3, -1, 8]])
    ans = np.array([6, 25, -11, 15])
    init = np.zeros(n)

    result = gauss_seidel_iterative_method(n, mat, ans, init)
    print("The approximate solutions obtained are: {res}".format(res=result))


if __name__ == '__main__':
    main()
