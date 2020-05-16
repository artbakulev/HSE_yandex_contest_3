import numpy as np


def prod_upper_avg_diagonal(matrix: np.array):
    aver, diag = np.average(matrix), matrix.diagonal()
    return np.prod(diag[diag > aver])


matrix = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        matrix.append(list(map(float, line.split())))

print(prod_upper_avg_diagonal(np.array(matrix)))
