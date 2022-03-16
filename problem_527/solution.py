from math import ceil, comb, floor

# This problem was asked by Microsoft.
#
# Write a program to determine how many distinct ways there are to create a
# max heap from a list of N given integers.
#
# For example, if N = 3, and our integers are [1, 2, 3], there are two ways,
# shown below.
#
#   3      3
#  / \    / \
# 1   2  2   1

# Questions:
# - Is the list of integers unique? 
#   For example, [2, 2, 3] only has one solution
#     3
#    / \
#   2   2
#   I will assume the integers are unique...
# - Do the heaps have to be balanced? I assume so given the answer.


def num_heaps(num_ints):
    # for N ints, we know have the max, and then C(N - 1, (N - 1) // 2) ways
    # to partition the remaining elements into two subheaps
    # we can apply the same process for each sub-heap. this does not avoid double
    # counting for repeated elements in the list.
    if num_ints in [0, 1, 2]:
        return 1

    left = ceil((num_ints - 1) / 2.0)
    right = floor((num_ints - 1) / 2.0)
    return comb(num_ints - 1, left) * num_heaps(left) * num_heaps(right)

def test_num_heaps():
    for i in range(10):
        nh = num_heaps(i)
        print(f"{i}: {nh}")

if __name__ == "__main__":
    test_num_heaps()