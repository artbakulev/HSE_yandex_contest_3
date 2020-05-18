import numpy as np


def expected_reward(array):
    a = np.arange(array.shape[0])
    return (a * array).sum()
