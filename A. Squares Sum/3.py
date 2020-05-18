import numpy


def get_squares(arr):
    result_arr = [item for item in arr if item > 0]
    return numpy.square(result_arr).sum()