

# This problem was asked by Apple.
# 
# A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.
# 
# For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.


def find_fixed_point(monotonic_array):
    """
    Use a modified binary search to identify if a fixed point exists.
    """
    if len(monotonic_array) == 0:
        return False
    idx = len(monotonic_array) // 2
    if monotonic_array[idx] > idx:
        return find_fixed_point(monotonic_array[:idx])
    elif monotonic_array[idx] < idx:
        return find_fixed_point(monotonic_array[idx+1:])
    else:
        return idx


def test_find_fixed_point():
    assert find_fixed_point([-6, 0, 2, 40]) == 2
    assert find_fixed_point([1, 5, 7, 8]) is False


if __name__ == "__main__":
    test_find_fixed_point()
