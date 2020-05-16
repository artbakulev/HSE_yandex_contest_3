import numpy as np


def get_squares(array: np.array):
    array_filter = array > 0
    return np.square(array[array_filter]).sum()


a = np.array(list(map(int, input().split(' '))))
print(get_squares(a))
