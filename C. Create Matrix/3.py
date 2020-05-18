import numpy as np


def create_ij(n):
    matrix = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i].append(i * j)
    return np.array(matrix)