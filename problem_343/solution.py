# This problem was asked by Google.
#
# Given a binary search tree and a range [a, b] (inclusive), return the sum of
# the elements of the binary search tree within the range.
#
# For example, given the following tree:
#
#     5
#    / \
#   3   8
#  / \ / \
# 2  4 6  10
# and the range [4, 9], return 23 (5 + 4 + 6 + 8).


class Tree:
    def __init__(self, value, left, right):
        self._value = value
        self._left = left
        self._right = right

    @property
    def value(self):
        return self._value

    @property
    def left(self):
        return self._left

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self._left = Tree(value, None, None)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self._right = Tree(value, None, None)

    @property
    def right(self):
        return self._right

    def __repr__(self):
        left_str = "" if not self.left else self.left.__repr__()
        right_str = "" if not self.right else self.right.__repr__()
        return f"({self.value}: {left_str}, {right_str})"


def upper_bound(tree, upper):
    if tree.value >= upper:
        if tree.left:
            Tree.upper_bound(tree.left, upper)
        else:
            return tree
    elif tree.value < upper:
        if tree.right:
            Tree.upper_bound(tree.right, upper)
        else:
            return None


def range_sum(tree, lower, upper):
    """
    A post-order traversal where we short-ciruit on lower/upper bounds.
    """
    if lower > upper:
        raise ValueError(
            f"Lower cannot be greater than upper. {lower}, {upper}."
        )

    total = 0
    if tree.left and tree.value >= lower:
        total += range_sum(tree.left, lower, upper)

    if tree.right and tree.value <= upper:
        total += range_sum(tree.right, lower, upper)

    if tree.value <= upper and tree.value >= lower:
        total += tree.value
    return total


def test_tree1():
    tree = Tree(3, None, None)
    tree.insert(2)
    tree.insert(1)
    tree.insert(4)
    tree.insert(5)
    return tree


def test_tree2():
    tree = Tree(
        5,
        Tree(3, Tree(2, None, None), Tree(4, None, None)),
        Tree(8, Tree(6, None, None), Tree(10, None, None)),
    )
    return tree


def test_range_sum():
    assert range_sum(test_tree1(), 4, 9) == 9
    assert range_sum(test_tree2(), 4, 9) == 23


if __name__ == "__main__":
    test_range_sum()
