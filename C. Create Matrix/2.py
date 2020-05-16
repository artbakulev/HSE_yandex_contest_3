import numpy as np


def print_matrix(n):
    for i in n:
        for number in i:
            print(number, end=' ')
        print()


def create_ij(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(i * j)
    return np.array(matrix)


print_matrix(create_ij(int(input())))
