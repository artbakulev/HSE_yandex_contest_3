import numpy


def expected_award(array):
    awards = numpy.arange(array.shape[0])
    return awards.dot(array).sum()


numbers, arr = input().split(), []
for number in numbers:
    arr.append(float(number))

print(expected_award(numpy.array(arr)))
