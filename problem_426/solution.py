# This problem was asked by Facebook.
# 
# Given a binary tree, return the level of the tree with minimum sum.


from typing import ValuesView


class Node:
    def __init__(self, val, left=None, right=None):
        self._val = val
        self._left = left
        self._right = right
    
    @property
    def val(self):
        return self._val

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right


def depth_sum(tree: Node):
    if not isinstance(tree, Node):
        raise ValueError("Expected input to be a tree.")
    total = []
    def _depth_helper(tree, depth):
        if len(total) <= depth:
            total.append(tree.val)
        else:
            total[depth] += tree.val
        if tree.left:
            _depth_helper(tree.left, depth+1)
        if tree.right:
            _depth_helper(tree.right, depth+1)
    
    _depth_helper(tree, 0) 
    return total.index(min(total))


def test_depth_sum():
    leaf_tree = Node(
        1000, 
        Node(3),
        Node(7)
    )
    assert depth_sum(leaf_tree) == 1

    root_tree = Node(
        1, 
        Node(3),
        Node(7)
    )
    assert depth_sum(root_tree) == 0

    imbalance_tree1 = Node(
        1000, 
        Node(3),
        Node(
            7, 
            Node(6),
            Node(2)
        )
    )
    assert depth_sum(imbalance_tree1) == 2

    imbalance_tree2 = Node(
        1000, 
        Node(3),
        Node(
            7, 
            Node(6),
            Node(6)
        )
    )
    assert depth_sum(imbalance_tree2) == 1

    try:
        depth_sum(None)
        assert False
    except ValueError:
        pass


if __name__ == "__main__":
    test_depth_sum()
