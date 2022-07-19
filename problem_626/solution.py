import heapq

# This problem was asked by Facebook.
# 
# Given a list of integers, return the largest product that can be made by
# multiplying any three integers.
# 
# For example, if the list is [-10, -10, 5, 2], we should return 500, since
# that's -10 * -10 * 5.
# 
# You can assume the list has at least three integers.


def find_largest_product(vals):
    # The largest product will use either the two largest, negative numbers
    # and the largest positive number, or it will use the 3 largest positive
    # numbers.
    assert len(vals) >= 3
    # heapq creates a min-heap by default
    largest = []  # min-heap
    smallest = []  # max-heap
    for v in vals:
        # pop and swap largest and smallest
        if len(smallest) == 2 and -1*v < smallest[0]:
            heapq.heappushpop(smallest, -1*v)
        else:
            heapq.heappush(smallest, -1*v)

        if len(largest) == 3 and v > largest[0]:
            heapq.heappushpop(largest, v)
        else:
            heapq.heappush(largest, v)

    return max(
        # -1's added at insertion cancel out.
        smallest[0]*smallest[1]*max(largest),
        largest[0]*largest[1]*largest[2],
    )


def test_find_largest_product():
    assert find_largest_product([-10, -10, 5, 2]) == 500


if __name__ == "__main__":
    test_find_largest_product()
