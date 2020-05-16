import numpy as np


def expected_award(array):
    return np.arange(array.size).dot(array).sum()


a = np.array(list(map(float, input().split())))
print(expected_award(a))
