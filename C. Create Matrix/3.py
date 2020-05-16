import numpy as np


def create_ij(n):
    matrix = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i].append(i * j)
    return np.array(matrix)


n = int(input())
m = create_ij(n)
for numbers in m:
    for number in numbers:
        print(number, end=' ')
    print()
