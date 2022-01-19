
# This problem was asked by Netflix.
#
# A Cartesian tree with sequence S is a binary tree defined by the following
# two properties:
#
# It is heap-ordered, so that each parent value is strictly less than that of
# its children. An in-order traversal of the tree produces nodes with values
# that correspond exactly to S. For example, given the sequence
# [3, 2, 6, 1, 9], the resulting Cartesian tree would be:
#
#       1
#     /   \   
#   2       9
#  / \
# 3   6
#
# Given a sequence S, construct the corresponding Cartesian tree


class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # @property
    # def value(self):
    #     return self._value
    
    # @property
    # def left(self):
    #     return self._left
    
    # @property
    # def right(self):
    #     return self._right
    
    def __repr__(self) -> str:
        str = "("
        if self.left:
            str += self.left.__repr__()
        str += f", {self.value}, "
        if self.right:
            str += self.right.__repr__()
        str += ")"
        return str


def cartesian_tree(sequence, start=float("-inf")):
    tree = Tree(sequence[0])
    # We will intially assume that we are building the right subtree of a heap
    # with an infinitely small value.

     # 1.) we know that the first value would be the left-most child
     # 2.) we know that the second node must be the parent of the first and is
     # guaranteed to be smaller.
     # 3.) any value that we encounter that is larger implies that we're
     # starting a new right child from an existing tree. It must be a right
     # child because this is an in-order traversal. so all values in the left
     # tree or parent have already been seen.

    for s in range(1, len(sequence)):
        v = sequence[s]
        
        # we reached the end of this right subtree
        if v < start:
            return tree

        # this starts a right subtree.
        if v >= tree.value:
            # we know that this right subtree will continue until we see the
            # next value that is smaller than v
            tree.right = cartesian_tree(sequence[s:], v)
            # In python this will actually create a copy of the sequence, we
            # should use a sequence-view type object instead or maybe produce
            # the values from a generator
        else:  # finished a left subtree
            tree = Tree(v, left=tree)
    return tree


def test_cartesian_tree():
    sequence = [3, 2, 6, 1, 9]
    tree = cartesian_tree(sequence)
    #       1
    #     /   \   
    #   2       9
    #  / \
    # 3   6
    print(tree)
    assert tree.value == 1
    assert tree.left.value == 2
    assert tree.left.left.value == 3
    assert tree.left.right.value == 6
    assert tree.right.value == 9


if __name__ == "__main__":
    test_cartesian_tree()
