import numpy as np
from src.linear_iterative_techniques.jacobi_iterative_technique import jacobi_iterative_technique


def main():
    n = 4
    mat = np.array([[10, -1, 2, 0],
                    [-1, 11, -1, 3],
                    [2, -1, 10, -1],
                    [0, 3, -1, 8]])
    ans = np.array([6, 25, -11, 15])
    init = np.zeros(n)

    result = jacobi_iterative_technique(n, mat, ans, init)
    print("The approximate solutions obtained are: {res}".format(res=result))


if __name__ == '__main__':
    main()
