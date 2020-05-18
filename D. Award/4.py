import numpy


def expected_reward(array):
    rewards = numpy.arange(len(array))
    return rewards.dot(array).sum()
