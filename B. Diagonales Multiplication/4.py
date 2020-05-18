import numpy as np


def prod_upper_avg_diagonal(matrix: np.array):
    diagonal = matrix.diagonal()
    average = np.average(matrix)
    return np.prod(diagonal[diagonal > average])

