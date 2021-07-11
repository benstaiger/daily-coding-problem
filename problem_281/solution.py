# This problem was asked by LinkedIn.
#
# A wall consists of several rows of bricks of various integer lengths and
# uniform height. Your goal is to find a vertical line going from the top to
# the bottom of the wall that cuts through the fewest number of bricks. If the
# line goes through the edge between two bricks, this does not count as a cut.
#
# For example, suppose the input is as follows, where values in each row
# represent the lengths of bricks in that row:
#
# [[3, 5, 1, 1],
#  [2, 3, 3, 2],
#  [5, 5],
#  [4, 4, 2],
#  [1, 3, 3, 3],
#  [1, 1, 6, 1, 1]]
#
# The best we can we do here is to draw a line after the eighth brick, which
# will only require cutting through the bricks in the third and fifth row.
#
# Given an input consisting of brick lengths for each row such as the one
# above, return the fewest number of bricks that must be cut to create a
# vertical line.


def find_cut(wall):
    """
    We will find the fewest number of bricks that need to be cut to create
    a vertical line.

    Assume that each row has a total length of N and that we have a total of
    B bricks in the wall. There are N-1 possible locations to cut. We will
    start by assuming that every location will take R cuts, equal to the
    number of rows. Then for every space we encounter, we will reduce the
    number of necessary cuts for a given position as we iterate through
    all of the bricks.

    This will require O(B + N) time to complete and O(N) space.
    There is likely not a better time complexity solution because this is
    essentially bounded on just reading the bricks unless we end up with
    a fairly degenerate case such as [[1e100]].
    """
    cuts = [len(wall) for i in range(sum(wall[0]) - 1)]
    # 0 indicates a cut after the first "1-unit" of brick.
    for row in wall:
        total_offset = 0
        # We do not include the last brick in a row because we do not allow
        # a cut at the end of the wall.
        for b in row[:-1]:
            total_offset += b
            cuts[total_offset - 1] -= 1
    return min(cuts)


def test_find_test():
    wall1 = [
        [10],
    ]
    assert find_cut(wall1) == 1
    wall2 = [
        [10],
        [5, 5],
    ]
    assert find_cut(wall2) == 1
    wall3 = [
        [10],
        [5, 5],
        [2, 3, 5],
    ]
    assert find_cut(wall3) == 1
    wall4 = [[5, 2, 3], [5, 5], [2, 3, 5]]
    assert find_cut(wall4) == 0
    wall5 = [[4, 3, 3], [5, 5], [2, 3, 5]]
    assert find_cut(wall5) == 1
    wall_example = [
        [3, 5, 1, 1],
        [2, 3, 3, 2],
        [5, 5],
        [4, 4, 2],
        [1, 3, 3, 3],
        [1, 1, 6, 1, 1],
    ]
    assert find_cut(wall_example) == 2


if __name__ == "__main__":
    test_find_test()
