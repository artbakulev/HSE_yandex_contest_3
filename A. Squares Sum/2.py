import numpy


def get_squares(arr):
    return numpy.square(arr[arr > 0]).sum()


a = numpy.array(list(map(int, input().split(' '))))
print(get_squares(a))
