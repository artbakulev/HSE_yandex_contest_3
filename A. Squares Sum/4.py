import numpy as np


def get_squares(arr):
    result = 0
    for i in arr:
        if i > 0:
            result += i**2
    return np.array(result)
