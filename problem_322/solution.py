from math import sqrt, ceil

# This problem was asked by Flipkart.
#
# Starting from 0 on a number line, you would like to make a series of jumps
# that lead to the integer N.
#
# On the ith jump, you may move exactly i places to the left or right.
#
# Find a path with the fewest number of jumps required to get from 0 to N.

def find_jumps(N: int):
    """
    We will find the total number of jumps in constant time.
    """
    N = abs(N)

    # start by finding the number of jumps where we would jump >= N
    # we can solve for this analytically.

    # We know that N = K * (K + 1) / 2 -> K**2 + K - 2N = 0
    # -> K = [-1 +/- sqrt(1**2 - 4*1*-2N)}/ 2*1
    # and we only care about the positive root.
    jumps = ceil((-1 + sqrt(1 + 8*N)) / 2)

    # If N is odd, we need to find the smallest ODD number >= N
    # If N is even, we need to find the smallest EVEN number >= N
    # This is because we can only make even spaced adjustments by reversing the
    # sign of any of the values in the sum so far.

    # We know that a total will be even if K or K + 1 is a multiple of 4 and
    # odd otherwise. Thus, we will only need to iterate at most 3 times.
    def sum_total(K: int):
        return K * (K + 1) // 2
    while (sum_total(jumps) - N) % 2 != 0:
        jumps += 1
    
    return jumps
    

def test_find_jumps():
    assert find_jumps(3) == 2
    assert find_jumps(6) == 3
    assert find_jumps(4) == 3  # -1 + 2 + 3


if __name__ == "__main__":
    test_find_jumps()

