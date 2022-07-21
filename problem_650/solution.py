
# This problem was asked by LinkedIn.
# 
# Determine whether a tree is a valid binary search tree.
# 
# A binary search tree is a tree with two children, left and right, and
# satisfies the constraint that the key in the left child must be less than or
# equal to the root and the key in the right child must be greater than or
# equal to the root.


class Tree():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_binary_tree(tree) -> "tuple[bool, int, int]":
    # As written, it doesn't actually state that ALL nodes in the left/right
    # tree need to be less/greater than the value of the root. But this is
    # the check that we will run because otherwise it really dosen't function
    # as a binary search tree... since this tree meets the local constraint,
    # but not the global one.
    #       10
    #   6       12
    # 5   11   _   _

    lower = tree.value
    upper = tree.value
    if tree.left:
        is_bst, bst_min, bst_max = is_binary_tree(tree.left)
        lower = min(lower, bst_min)
        if not is_bst or tree.left.value > tree.value or bst_max > tree.value:
            return False, None, None
    if tree.right:
        is_bst, bst_min, bst_max = is_binary_tree(tree.right)
        upper = max(upper, bst_max)
        if not is_bst or tree.right.value < tree.value or bst_min < tree.value:
            return False, None, None
    return True, lower, upper


def test_is_bst():
    not_bst = Tree(
        10,
        left = Tree(
            6,
            left = Tree(5),
            right = Tree(11)
        ),
        right = Tree(12)
    )
    is_bst = Tree(
        10,
        left = Tree(
            6,
            left = Tree(5),
            right = Tree(9)
        ),
        right = Tree(12)
    )
    check, _, _ = is_binary_tree(not_bst)
    assert check is False

    check, lower, upper = is_binary_tree(is_bst)
    assert check is True
    assert lower == 5 and upper == 12


if __name__ == "__main__":
    test_is_bst()
