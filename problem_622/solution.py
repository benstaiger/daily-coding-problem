# This problem was asked by Google.
#
# Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.
#
#     a
#    / \
#   b   c
#  /
# d


class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def deepest_node(tree):
    def deepest(tree, current_depth):
        deep = (current_depth, tree.value)
        if tree.left:
            deep = deepest(tree.left, current_depth + 1)
        if tree.right:
            depth, value = deepest(tree.right, current_depth + 1)
            if depth > deep[0]:
                deep = depth, value
        return deep

    _, v = deepest(tree, 0)
    return v


def test_deepest_node():
    example = Tree("a", left=Tree("b", left=Tree("d")), right=Tree("c"))
    assert deepest_node(example) == "d"


if __name__ == "__main__":
    test_deepest_node()
