import numpy as np


def expected_award(array):
    awards = np.arange(array.shape[0])
    return awards.dot(array).sum()


a = np.array(list(map(float, input().strip().split())))
print(expected_award(a))
