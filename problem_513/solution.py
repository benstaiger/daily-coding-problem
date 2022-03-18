
# This problem was asked by Lyft.
# 
# Given a list of integers and a number K, return which contiguous elements
# of the list sum to K.
# 
# For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return
# [2, 3, 4], since 2 + 3 + 4 = 9.


def contiguous_sum(values, target):
    # Use two pointers to construct an expanding/contracting window
    # of values.

    # for every index, i, in the array, the largest (sum) subarray containing
    # will be considered. Implying that if such a subarray exists, it will be
    # located because the largest subarray starting at its first element is
    # guaranteed to be considered.

    # this assumes that all values are positive!
    i = 0
    j = 1
    total = values[0]
    while i < len(values):
        if total > target:
            total -= values[i]
            i += 1
            if j <= i:
                j += 1
        elif total < target:
            if j < len(values):
                total += values[j]
                j += 1
            else:
                break
        elif total == target:
            return values[i:j]
    return None


def test_contiguous_sum():
    # For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return
    # [2, 3, 4], since 2 + 3 + 4 = 9.
    example = [1, 2, 3, 4, 5]
    assert contiguous_sum(example, 9) in [[2, 3, 4], [4, 5]]

    example = [1, 2, 3, 4, 5]
    assert contiguous_sum(example, 52) is None

    example = [1, 2, 3, 4, 5]
    assert contiguous_sum(example, sum(example)) == example

    example = [1, 2, 3, 4, 5, 6]
    assert contiguous_sum(example, 11) == [5, 6]

    example = [1, 2, 3, 4, 5, 6]
    assert contiguous_sum(example, -11) is None


if __name__ == "__main__":
    test_contiguous_sum()
