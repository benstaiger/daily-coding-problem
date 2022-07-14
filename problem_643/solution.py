
# This problem was asked by Google.
# 
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# 
# Given the root to a binary tree, count the number of unival subtrees.
# 
# For example, the following tree has 5 unival subtrees:
# 
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_unival_tree(root):
    """
    Return whether this root is itself a unival tree and how many unival 
    subtrees it has.
    """
    is_unival = True
    unival_trees = 0
    if root.left:
        uni, num = is_unival_tree(root.left)
        unival_trees += num
        if uni and root.value != root.left.value:
            is_unival = False
    if root.right:
        uni, num = is_unival_tree(root.right)
        unival_trees += num
        if uni and root.value != root.right.value:
            is_unival = False
    if is_unival:
        unival_trees += 1
    return is_unival, unival_trees


def test_is_unival_tree():
    example = TreeNode(
        0,
        left = TreeNode(1),
        right = TreeNode(
            0,
            left = TreeNode(
                1,
                left = TreeNode(1),
                right = TreeNode(1)
            ),
            right = TreeNode(0)
        )
    )
    assert is_unival_tree(example) == (False, 5)


if __name__ == "__main__":
    test_is_unival_tree()