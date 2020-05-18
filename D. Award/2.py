import numpy as np


def expected_reward(array):
    return np.arange(array.size).dot(array).sum()
