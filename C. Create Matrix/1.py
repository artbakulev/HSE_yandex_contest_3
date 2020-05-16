import numpy as np


def create_ij(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(i * j)
    return np.array(matrix)


n = int(input())
m = create_ij(n)
for i in m:
    for number in i:
        print(number, end=' ')
    print()
