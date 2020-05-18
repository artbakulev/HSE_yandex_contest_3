import numpy as np


def prod_upper_avg_diagonal(matrix: np.array):
    average = np.average(matrix)
    diagonal = matrix.diagonal()
    diagonal_filter = diagonal > average
    return np.prod(diagonal[diagonal_filter])


with open('input.txt', 'r') as f:
    lines = f.readlines()

matrix = []
for line in lines:
    matrix.append(list(map(float, line.strip().split())))
matrix = np.array(matrix)

print(prod_upper_avg_diagonal(matrix))
