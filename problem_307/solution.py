from typing import Optional


class Tree:
    def __init__(self, left: "Tree", right: "Tree", val: int):
        self._left = left
        self._right = right
        self._val = val

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def val(self):
        return self._val


def find_bounds(tree: Tree, val: int):
    # an algorithm for this type of thing essentially already exists in most
    # languages. std::lower(upper)_bound in C++ and bisect.bisect_left(right)
    # in python.
    # While neighter explicity work on a "tree" structure it essentially
    # performs this function via binary search on an array or sequential
    # search for iterable, but not indexible structures in c++
    last_right = None
    last_left = None

    def find_bounds(tree, val):
        if tree.val > val:
            if tree.left:
                last_left = tree
                return floor(tree.left, val)
            else:
                return None
        elif tree.val == val:
            return tree
        else:
            if tree.right:
                last_right = tree
                return floor(tree.right, val)
            else:
                return None

    val = find_bounds(tree, val)
    return last_left, val, last_right


def floor(tree: Tree, val: int):
    lower, val, _ = find_bounds(tree, val)
    return val if val else lower


def ceiling(tree: Tree, val: int):
    _, val, upper = find_bounds(tree, val)
    return val if val else upper


def test_floor(tree: Tree, val: int):
    pass


def test_ceiling():
    pass


if __name__ == "__main__":
    test_floor()
    test_ceiling()
