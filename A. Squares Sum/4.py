import numpy


def get_squares(arr):
    result = 0
    for i in arr:
        if i > 0:
            result += i**2
    return result


a = numpy.array(list(map(int, input().split(' '))))
print(get_squares(a))
