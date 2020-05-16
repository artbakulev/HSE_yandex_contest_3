import numpy as np


def prod_upper_avg_diagonal(matrix: np.array):
    diagonal = matrix.diagonal()
    average = np.average(matrix)
    return np.prod(diagonal[diagonal > average])


matrix = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        temp = []
        for num in line.split():
            temp.append(float(num))
        matrix.append(temp)
    matrix = np.array(matrix)

print(prod_upper_avg_diagonal(matrix))
