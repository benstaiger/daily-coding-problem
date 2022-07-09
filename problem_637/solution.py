# This problem was asked by Snapchat.
# 
# Given a list of possibly overlapping intervals, return a new list of
# intervals where all overlapping intervals have been merged.
# 
# The input list is not necessarily ordered in any way.
# 
# For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return
# [(1, 3), (4, 10), (20, 25)].


def merge_intervals(intervals):
    # I don't think that there is any way to do this in less than O(nlogn)
    intervals = sorted(intervals)
    
    # for each intervals, check if it overlaps with the last interval 
    new_ivals = [intervals[0]]
    for ival in intervals[1:]:
        # I will assume that intervals are open on both ends.
        if ival[0] < new_ivals[-1][1]:
            new_ivals[-1] = (new_ivals[-1][0], max(ival[1], new_ivals[-1][1]))
        else:
            new_ivals.append(ival)
    return new_ivals


def test_merge():
    assert merge_intervals([(1, 3), (5, 8), (4, 10), (20, 25)]) == [(1, 3), (4, 10), (20, 25)]


if __name__ == "__main__":
    test_merge()
