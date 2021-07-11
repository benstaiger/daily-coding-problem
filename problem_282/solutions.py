# This problem was asked by Netflix.
#
# Given an array of integers, determine whether it contains a Pythagorean
# triplet. Recall that a Pythogorean triplet (a, b, c) is defined by the
# equation a2+ b2= c2.


def pythogorean_triple(numbers):
    """
    Look for a pythogorean triple in a list of numbers.
    """
    squares = sorted([x ** 2 for x in numbers])

    # Assume that a <= b <= c
    # We will start at the largest c, then iteratively search
    # for an appropriate a and b depending on whether our current
    # value is too small or too large.

    # So, for each c we will look at atmost N values of a and b meaning
    # that our total search will be O(N^2)
    for idx_c in range(len(squares) - 1, 2, -1):
        idx_a = 0
        idx_b = idx_c - 1
        while idx_a < idx_b:
            if squares[idx_a] + squares[idx_b] > squares[idx_c]:
                idx_b -= 1
            elif squares[idx_a] + squares[idx_b] < squares[idx_c]:
                idx_a += 1
            if squares[idx_a] + squares[idx_b] == squares[idx_c]:
                print(
                    f"{squares[idx_a]} + {squares[idx_b]} == {squares[idx_c]}"
                )
                return True
    return False


def test_pythogorean_triple():
    assert pythogorean_triple(range(10)) is True  # (0, 2, 4) or (3, 4, 5)
    assert pythogorean_triple(range(1, 5)) is False


if __name__ == "__main__":
    test_pythogorean_triple()
