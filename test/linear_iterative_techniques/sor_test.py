import numpy as np
from src.linear_iterative_techniques.sor import sor


def main():
    n = 3
    mat = np.array([[4, 3, 0],
                    [3, 4, -1],
                    [0, -1, 4]])

    ans = np.array([24, 30, -24])
    init = np.ones(n)

    result = sor(n, mat, ans, init, 1.25)
    print("The approximate solutions within given precision are: {res}".format(res=result))


if __name__ == '__main__':
    main()
