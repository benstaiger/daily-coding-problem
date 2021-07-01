import doctest
from itertools import accumulate

# This problem was asked by Spotify.
#
# Write a function, throw_dice(N, faces, total), that determines how many ways
# it is possible to throw N dice with some number of faces each to get a
# specific total.
#
# For example, throw_dice(3, 6, 7) should equal 15.


def printer(func):
    def wrapper_print(N, faces, total):
        v = func(N, faces, total)
        print(f"throw_dice({N}, {faces}, {total}) = {v}")
        return v

    return wrapper_print


def throw_dice_recursive(N, faces, total):
    """
    determines how many ways it is possible to throw N dice with some number
    of faces each to get a specific total.
    >>> throw_dice_recursive(3, 6, 7)
    15
    >>> throw_dice_recursive(3, 6, 18)
    1
    >>> throw_dice_recursive(3, 6, 2)
    0
    >>> throw_dice_recursive(3, 6, 19)
    0
    >>> throw_dice_recursive(3, 6, -1)
    0
    """
    # simple recurrsive DP.
    assert N > 0 and faces > 0
    if N > 1:
        ways = [
            throw_dice_recursive(N - 1, faces, total - i)
            for i in range(1, faces + 1)
        ]
        #    print(ways)
        return sum(ways)
    elif total > faces or total <= 0:
        return 0
    else:
        return 1


def throw_dice_iterative(N, faces, total):
    """
    determines how many ways it is possible to throw N dice with some number
    of faces each to get a specific total.
    >>> throw_dice_iterative(3, 6, 7)
    15
    >>> throw_dice_iterative(3, 6, 18)
    1
    >>> throw_dice_iterative(3, 6, 2)
    0
    >>> throw_dice_iterative(3, 6, 19)
    0
    >>> throw_dice_iterative(3, 6, -1)
    0
    >>> throw_dice_iterative(1, 6, 5)
    1
    >>> throw_dice_iterative(2, 6, 7)
    6
    """
    # Dynamic programming solution: Create a table of how many ways there are
    # to get a specific total and accumulate.

    if N <= 0 or faces <= 0 or total <= 0:
        return 0

    ways = [[0 for t in range(total + 1)] for d in range(N + 1)]
    ways[1] = [1 if t > 0 and t <= faces else 0 for t in range(total + 1)]
    for d in range(2, N + 1):
        rolling = list(accumulate(ways[d - 1]))
        for t in range(1, total + 1):
            if t <= faces:
                ways[d][t] = rolling[t - 1]
            else:
                ways[d][t] = rolling[t - 1] - rolling[t - faces - 1]
    return ways[N][total]


if __name__ == "__main__":
    doctest.testmod()
