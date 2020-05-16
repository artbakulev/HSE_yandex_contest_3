import numpy as np


def create_ij(n):
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matrix[i][j] = i * j
    return matrix


matr = create_ij(int(input()))
for row in matr:
    for number in row:
        print(str(int(number)) + ' ', end='')
    print()
