import math
import random

# This problem was asked by Dropbox.
# 
# Create an algorithm to efficiently compute the approximate median of a list
# of numbers.
# 
# More precisely, given an unordered list of N numbers, find an element whose
# rank is between N / 4 and 3 * N / 4, with a high level of certainty, in less
# than O(N) time.


def simple_median(data):
    d = sorted(data)
    return d[len(d)//2]

def approx_median(data):
    # so we basically have O(logN)
    # median finding can typically be done on average O(N) worst case NlogN
    # with intro-select, or approximate median finding with quickselect in O(N)

    # randomly select O(logN) elements
    num_elements = 5 * math.ceil(math.log(len(data)))
    sample = [data[random.randrange(0, len(data))] for _ in range(num_elements)]

    # return the median of the sample

    # this succeeds as long as there aren't more than num_elements/2 less than N/4
    # or greater than 3*N/4. The probability of drawing an individual elements w/
    # replacement less than N/4 is 0.25.
    # so prob of getting at least k/2 = num_elements/2 of them is
    # sum(C(i, K) * 0.25^i * 0.75^(k-i), i from k/2 to k)
    # and similarly for the upper side.

    return simple_median(sample)
