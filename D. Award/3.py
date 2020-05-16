import numpy as np


def expected_award(array):
    awards = np.arange(array.shape[0])
    return (awards * array).sum()


line, arr = input().split(), []
for num in line:
    arr.append(float(num))

print(expected_award(np.array(arr)))
