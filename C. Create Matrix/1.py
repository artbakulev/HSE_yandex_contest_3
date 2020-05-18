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
result = ''
for i in m:
    for num in i:
        result += str(num) + ' '
    result = result.rstrip()
    result += '\n'
result = result.strip()
print(result)