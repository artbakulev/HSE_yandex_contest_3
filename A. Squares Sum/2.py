import numpy


def get_squares(arr):
    return numpy.square(arr[arr > 0]).sum()
