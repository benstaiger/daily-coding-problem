
# This problem was asked by Yelp.
# 
# You are given an array of integers, where each element represents the maximum
# number of steps that can be jumped going forward from that element. Write a
# function to return the minimum number of jumps you must take in order to get
# from the start to the end of the array.
# 
# For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, as
# the optimal solution involves jumping from 6 to 5, and then from 5 to 9.


def jumps_to(values):
    # In a dynamic programming approach, find the minimum number of jumps
    # to reach a given location.

    # O(N)
    jumps = 0
    current_reachable = 0
    furthest_reachable = 0
    for i, v in enumerate(values):
        if i > current_reachable:
            jumps += 1
            current_reachable = furthest_reachable
        furthest_reachable = max(furthest_reachable, i + v)
    return jumps


def test_jumps_to():
    # For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, as
    # the optimal solution involves jumping from 6 to 5, and then from 5 to 9.
    assert jumps_to([6, 2, 4, 0, 5, 1, 1, 4, 2, 9]) == 2
    assert jumps_to(range(1, 6)) == 3


if __name__ == "__main__":
    test_jumps_to()
