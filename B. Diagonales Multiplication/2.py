import numpy as np


def prod_upper_avg_diagonal(matrix: np.array):
    aver, diag = np.average(matrix), matrix.diagonal()
    return np.prod(diag[diag > aver])

