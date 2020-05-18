import numpy as np


def prod_upper_avg_diagonal(matrix: np.array):
    average = np.average(matrix)
    diagonal = matrix.diagonal()
    f = diagonal > average
    return np.prod(diagonal[f])
