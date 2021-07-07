from functools import lru_cache

# This problem was asked by Amazon.
#
# Given an integer N, construct all possible binary search trees with N nodes.


class Tree:
    def __init__(self, left, right, value=None):
        self._left = left
        self._right = right
        self._value = value

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def value(self):
        return self._value

    def __repr__(self):
        return f"<{self.value}>({self.left}, {self.right})"


def cache_demonstration(func):
    cache = {}

    def wrapped_func(*args):
        if args in cache:
            res = cache[args]
        else:
            res = func(*args)
            cache[args] = res
        return res

    return wrapped_func


# @lru_cache(maxsize=None)  # short circuit recomputing subtrees
@cache_demonstration  # short circuit recomputing subtrees
def construct_trees(N, value_offset=0):
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
            for t2 in construct_trees(N - i - 1):
                results.append(Tree(t1, t2))

    # If they require that we actually add values to the trees. This can
    # be simply done after-the-fact by doing an inorder traversal and adding
    # values to each node in order.
    return results


if __name__ == "__main__":
    print(construct_trees(3))
    # total number of trees is

