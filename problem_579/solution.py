from math import sqrt, ceil

# This problem was asked by Flipkart.
# 
# Starting from 0 on a number line, you would like to make a series of jumps that lead to the integer N.
# 
# On the ith jump, you may move exactly i places to the left or right.
# 
# Find a path with the fewest number of jumps required to get from 0 to N.


def min_jumps(target):
    # There are two cases 1: target = sum(i, i=1..N) = N * (N + 1) / 2
    # If it is not exact, then there exists a sum slightly larger than
    # target, but we know that sum - target < N, so we can simply flip a single
    # number in the sequence.

    # find N s.t. sum(i, i=1..N) bounds target from above.
    # 0 = N^2 + N - target*2
    # -> N = (-b +/- sqrt(b^2 - 4ac)) / 2a
    # -> N = (-1 +/- sqrt(1 + 4*1*target*2)) / 2
    N = ceil((-1 + sqrt(1 + 8 * target)) / 2)
    to_flip = N * (N + 1) / 2 - target
    return N


def test_min_jumps():
    for i in range(1, 10):
        print(i, min_jumps(i))


if __name__ == "__main__":
    test_min_jumps()
