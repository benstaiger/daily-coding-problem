from typing import Optional

# This problem was asked by PayPal.
# 
# Given a binary tree, determine whether or not it is height-balanced. A
# height-balanced binary tree can be defined as one in which the heights of the
# two subtrees of any node never differ by more than one.


class TreeNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def balanced_height(tree: TreeNode) -> Optional[int]:
    """Returns the height if the tree is balanced otherwise None"""
    left_height= 0
    if tree.left:
        left_height = balanced_height(tree.left)
    right_height= 0 
    if tree.right:
        right_height = balanced_height(tree.right)
    if left_height is None or right_height is None or abs(left_height - right_height) > 1:
        return None
    return 1 + max(left_height, right_height)


def is_height_balanced(tree):
    return not balanced_height(tree) is None


def test_balanced_height():
    simple = TreeNode(
        TreeNode(),
        TreeNode()
    )
    assert balanced_height(simple) == 2
    simple = TreeNode(
        TreeNode(),
        TreeNode(TreeNode())
    )
    assert balanced_height(simple) == 3
    simple = TreeNode(
        TreeNode(),
        TreeNode(TreeNode(), TreeNode(TreeNode()))
    )
    assert balanced_height(simple) is None
    simple = TreeNode(
        TreeNode(TreeNode()),
        TreeNode(TreeNode(), TreeNode())
    )
    assert balanced_height(simple) == 3
    simple = TreeNode(
        TreeNode(TreeNode(TreeNode()), TreeNode()),
        TreeNode(TreeNode(), TreeNode())
    )
    assert balanced_height(simple) == 4
    simple = TreeNode(
        TreeNode(TreeNode(TreeNode(TreeNode())),),
        TreeNode(TreeNode())
    )
    assert balanced_height(simple) is None


if __name__ == "__main__":
    test_balanced_height()
