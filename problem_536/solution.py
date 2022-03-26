
# This problem was asked by Google.
# 
# Given the sequence of keys visited by a postorder traversal of a binary
# search tree, reconstruct the tree.
# 
# For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the
# following tree:
# 
#     5
#    / \
#   3   7
#  / \   \
# 2   4   8

# (5: (7: (3: (2, 4)), 8), )

#     5
#    / \
#   3   7
#  / \   \
# 2   4   8
#    / \
#  3.5  4.5

# [2, 3.5, 4.5, 4, 3, 8, 7, 5]

# is a reversed post-order traversal a valid pre-order traversal?
# it seems like it... where we iter

class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"{self.value}: ({self.left}, {self.right})"


def post_order_construction(sequence):
    # if we're less than the prev, we must have finished a subtree
    # a reversed post-order traversal is a pre-order traversal where
    # we first construct the right subtree

    seq = list(reversed(sequence))
    
    def pre_order_helper(sequence, start_idx, stop_value):
        # Defines a point to stop iterating in the sequence
        # To identify when a tree has ended.
        tree = Tree(sequence[start_idx])
        start_idx += 1

        # Idenfify that we are a leaf?
        if start_idx < len(sequence) and sequence[start_idx] <= stop_value:
            return start_idx, tree

        # if the next value is greater, it is part of a right child
        if start_idx < len(sequence) and sequence[start_idx] > tree.value:
            start_idx, right = pre_order_helper(sequence, start_idx, tree.value)
            tree.right = right

        # check if we are lacking a left child
        if start_idx < len(sequence) and sequence[start_idx] <= stop_value:
            return start_idx, tree

        # if we have exhausted our right subtree, it must be 0
        # assert start_idx < len(sequence) and sequence[start_idx] <= tree.value

        if start_idx < len(sequence) and sequence[start_idx] <= tree.value:
            start_idx, left = pre_order_helper(sequence, start_idx, stop_value)
            tree.left = left
        
        return start_idx, tree

    i, tree = pre_order_helper(seq, 0, float("-inf"))
    assert i == len(sequence)
    return tree

# [5, 7, 8, 3, 4, 4.5, 3.5, 2] pre-order, right first

#     5
#    / \
#   3   7
#  / \   \
# 2   4   8
#    / \
#  3.5  4.5

# [2, 3.5, 4.5, 4, 3, 8, 7, 5]

def test_post_order():
    tree = post_order_construction([2, 3.5, 4.5, 4, 3, 8, 7, 5])
    str_repr = "5: (3: (2: (None, None), 4: (3.5: (None, None), 4.5: (None, None))), 7: (None, 8: (None, None)))"
    assert str(tree) == str_repr


if __name__ == "__main__":
    test_post_order()
