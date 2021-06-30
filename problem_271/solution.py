import doctest

# This problem was asked by Netflix.
#
# Given a sorted list of integers of length N, determine if an element x is in
# the list without performing any multiplication, division, or bit-shift
# operations.
# Do this in O(log N) time.


def special_binary_search(sorted_values, value):
    """
    This function provides a modified version of binary search where we start
    the beginning of the array and increment by powers of 2 until we pass the
    desired element or have isolated it to the last chunk of the array where
    making another step would overshoot the end of the array. Then we home-in
    on it by using gradually smaller power of 2. This essentially functions the
    same as a binary search once we have identified out first partition to
    start drilling down into.

    This is always guaranteed to be able to look over all values because
    2^N - 1 = SUM(2^i, for i in [0, N-1]). Can make this proof by induction.

    >>> special_binary_search(range(15), 6)
    6
    >>> special_binary_search(range(15), 15) is None
    True
    >>> special_binary_search(range(1), 1) is None
    True
    >>> special_binary_search(range(2), 1)
    1
    >>> special_binary_search(range(1), 0)
    0
    >>> special_binary_search([], 0) is None
    True
    """
    if len(sorted_values) == 0:
        return None

    increments = [1]
    current_increment = increments[-1]
    current_index = 0
    while (
        current_index + current_increment < len(sorted_values)
        and sorted_values[current_index] < value
    ):
        current_index += current_increment
        current_increment += current_increment
        increments.append(current_increment)

    # normal binary search
    increments.reverse()
    for step in increments:
        if sorted_values[current_index] < value and current_index + step < len(
            sorted_values
        ):
            current_index += step
        elif (
            sorted_values[current_index] > value and current_index - step >= 0
        ):
            current_index -= step
        elif sorted_values[current_index] == value:
            return current_index
    if sorted_values[current_index] == value:
        return current_index
    return None


if __name__ == "__main__":
    doctest.testmod()
