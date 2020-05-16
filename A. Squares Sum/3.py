import numpy


def get_squares(arr):
    return numpy.square(arr[arr > 0]).sum()


inp = input().split()
arr = []
for i in inp:
    arr.append(int(i))
a = numpy.array(arr)
print(get_squares(a))
