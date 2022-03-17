
# This problem was asked by Microsoft.
# 
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
# 
# For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element
# sequence is [1, 2, 3, 4]. Return its length: 4.
# 
# Your algorithm should run in O(n) complexity.


def longest_list(vals):
    hashed_idx = {}
    min_seen = float("-inf")
    for i, v in enumerate(vals):
        hashed_idx[v] = i
        min_seen = min(min_seen, v)
    
    seen = [False for _ in vals]
    def test_sequence_length(v):
        while v in hashed_idx:
            seen[hashed_idx[v]] = True
            v += 1
        v_max = v - 1
        v -= 1
        while v in hashed_idx:
            seen[hashed_idx[v]] = True
            v -= 1
        v_min = v + 1

        return v_max - v_min + 1

    best_length = 1
    for idx, v in enumerate(vals):
        if not seen[idx]:
            best_length = max(best_length, test_sequence_length(v))
    return best_length


def test_longest_list():
    # For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element
    # sequence is [1, 2, 3, 4]. Return its length: 4.
    example = [100, 4, 200, 1, 3, 2]
    assert longest_list(example) == 4


if __name__ == "__main__":
    test_longest_list()
