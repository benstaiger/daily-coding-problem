
# This question was asked by Apple.
# 
# Given a binary tree, find a minimum path sum from root to a leaf.
# 
# For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.
# 
#   10
#  /  \
# 5    5
#  \     \
#    2    1
#        /
#      -1

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_min_path(tree):
    min_children = float("inf")
    if tree.left:
        min_children = min(find_min_path(tree.left), min_children)
    if tree.left:
        min_children = min(find_min_path(tree.right), min_children)
    
    if min_children == float("inf"):
        return tree.value
    else:
        return tree.value + min_children


def test_min_path():
    #   10
    #  /  \
    # 5    5
    #  \     \
    #    2    1
    #        /
    #      -1
    tree = TreeNode(
        10,
        left = TreeNode(5, right=TreeNode(2)),
        right = TreeNode(5, right=TreeNode(1, left=TreeNode(-1)))
    )
    assert find_min_path(tree) == 15


if __name__ == "__main__":
    test_min_path()
