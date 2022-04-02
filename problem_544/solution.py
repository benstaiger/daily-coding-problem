# This problem was asked by Google.
#
# Given a list of integers S and a target number k, write a function that
# returns a subset of S that adds up to k. If such a subset cannot be made,
# then return null.
#
# Integers can appear more than once in the list. You may assume all numbers in
# the list are positive.
#
# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1]
# since it sums up to 24.


def sum_set(data, target):
    possible = [-1 for _ in range(target + 1)]
    possible[0] = 0

    # Find that it is possible in O(n*target) time and O(target) space
    for d in data:
        more_possible = possible.copy()
        for i in range(target + 1):
            # Check that we don't currently have a method of summing up to i
            if i - d >= 0 and possible[i - d] >= 0 and possible[i] < 0:
                more_possible[i] = d
        possible = more_possible
        if possible[target] >= 0:
            break

    if possible[target] < 0:
        return None

    t = target
    subset = []
    while t > 0:
        subset.append(possible[t])
        t = t - subset[-1]
    return subset


def test_sum_set():
    example = [12, 1, 61, 5, 9, 2]
    target = 24
    assert sorted(sum_set(example, target)) == [1, 2, 9, 12]

    example = [12, 1, 61, 5, 9, 2]
    target = 4
    assert sum_set(example, target) is None


if __name__ == "__main__":
    test_sum_set()
