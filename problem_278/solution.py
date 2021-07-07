from functools import lru_cache

# This problem was asked by Amazon.
#
# Given an integer N, construct all possible binary search trees with N nodes.


class Tree():
    def __init__(self, left, right):
        self._left = left
        self._right = right

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    def __repr__(self):
        return f"({self.left}, {self.right})"


@lru_cache(maxsize=None)  # short circuit recomputing subtrees
def construct_trees(N):
    """
    Constructs all possible trees of size N
    """
    if N == 0:
        return [None]
    results = []
    # i is the number of trees on the right side, N-i-1 is the number of
    # trees on the left side
    for i in range(N):
        print(f"Total: {N} left: {i}. right: {N-i-1}")
        for t1 in construct_trees(i):
            for t2 in construct_trees(N-i-1):
                results.append(Tree(t1, t2))

    return results


if __name__ == "__main__":
    print(construct_trees(3))
