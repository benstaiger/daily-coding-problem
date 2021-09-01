import itertools


# This problem was asked by LinkedIn.
#
# You are given a string consisting of the letters x and y, such as xyxxxyxyy.
# In addition, you have an operation called flip, which changes a single x to y
# or vice versa.
#
# Determine how many times you would need to apply this operation to ensure
# that all x's come before all y's. In the preceding example, it suffices to
# flip the second and sixth characters, so you should return 2.


def num_flips(x, y, sequence):
    if not sequence:
        raise ValueError("Passed an empty sequence.")
    if not all([i == x or i == y for i in sequence]):
        raise ValueError(f"Sequence contains characters other than {x}, {y}")

    # first we will find the number of x's up to every point in the sequence.
    cum_xs = list(
        itertools.accumulate(
            sequence, lambda a, b: a + 1 if b == x else a, initial=0
        )
    )
    # we start at 0, the number of x's up to the point just before the array.
    cum_xs.append(
        cum_xs[-1]
    )  # number of x's to the point just after the array.

    # For a given point including k, we know that we need to flip (k) - cum_xs[k]
    # values.
    # We also know that there are xs = cum_xs[-1] - cum_xs[k] x's after k that
    # need to be flipped.
    cost = [
        (k - cum_xs[k]) + (cum_xs[-1] - cum_xs[k]) for k in range(len(cum_xs))
    ]
    print(sequence, cum_xs, cost)
    return min(cost)


def test_num_flips_given():
    assert num_flips("x", "y", "xyxxxyxyy") == 2


def test_num_flips_trivial():
    assert num_flips("x", "y", "xyyyyyy") == 0


def test_num_flips_trivial2():
    assert num_flips("x", "y", "yyyyyyy") == 0
    assert num_flips("x", "y", "xxxxxxx") == 0


def test_num_flips_trivial3():
    assert num_flips("x", "y", "yxyyyyy") == 1


def test_num_flips_invalid():
    try:
        num_flips("x", "y", "") == 1
        assert False
    except ValueError:
        pass
    try:
        num_flips("x", "y", "xxxy1") == 1
        assert False
    except ValueError:
        pass


if __name__ == "__main__":
    test_num_flips_given()
    test_num_flips_trivial()
    test_num_flips_trivial2()
    test_num_flips_trivial3()
    test_num_flips_invalid()

