
# This problem was asked by Google.
# 
# You are given an array of nonnegative integers. Let's say you start at the
# beginning of the array and are trying to advance to the end. You can advance
# at most, the number of steps that you're currently on. Determine whether you
# can get to the end of the array.
# 
# For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices
# 0 -> 1 -> 3 -> 5, so return true.
# 
# Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.


def furthest_index(values):
    # for each index we will determine what is the furthest we can reach
    # in a dynamic programming fashion.
    reach = [0 for _ in values]
    furthest_reachable = reach[0]
    for i, v in enumerate(values):
        if i > furthest_reachable:
            return False
        reach[i] = i + v
        furthest_reachable = max(furthest_reachable, reach[i])
    
    return True


def test_furthest_index():
    # For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices
    # 0 -> 1 -> 3 -> 5, so return true.
    # 
    # Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
    assert furthest_index([1, 3, 1, 2, 0, 1])
    assert furthest_index([1, 2, 1, 0, 0]) is False


if __name__ == "__main__":
    test_furthest_index()
