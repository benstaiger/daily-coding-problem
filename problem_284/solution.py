# This problem was asked by Yext.
#
# Two nodes in a binary tree can be called cousins if they are on the same
# level of the tree but have different parents. For example, in the following
# diagram 4 and 6 are cousins.
#
#     1
#    / \
#   2   3
#  / \   \
# 4   5   6
#
# Given a binary tree and a particular node, find all cousins of that node.


class Node:
    def __init__(self, value, left, right):
        self._value = value
        self._left = left
        self._right = right

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def value(self):
        return self._value


def find_cousins(tree, node):
    """
    Find all nodes in a tree that are cousins of a given node.
    This is equivalent to finding all nodes at a given depth of the tree.

    This algorithm makes the assumption thtat the value in the tree is unique,
    but the tree is not necessarily in the order of a BST.
    """

    # Step 1: find the depth of the node.
    def in_order_traversal(node, value, depth=0):
        if node.value == value:
            return depth

        if node.left is not None:
            node_found = in_order_traversal(node.left, value, depth + 1)
            if node_found is not None:
                return node_found

        if node.right is not None:
            node_found = in_order_traversal(node.right, value, depth + 1)
            if node_found is not None:
                return node_found
        return None

    depth = in_order_traversal(tree, node)

    # Step 2: find all nodes at a given depth
    def bfs(tree, target_depth):
        to_traverse = [tree]
        for i in range(target_depth):
            next_layer = []
            for subtree in to_traverse:
                if subtree.left is not None:
                    next_layer.append(subtree.left)
                if subtree.right is not None:
                    next_layer.append(subtree.right)
            to_traverse = next_layer
        return to_traverse

    return [n.value for n in bfs(tree, depth) if n.value != node]


def test_find_cousins():
    tree = Node(
        1,
        Node(2,
             Node(4, None, None),
             Node(5, None, None)
             ),
        Node(3,
             None,
             Node(6, None, None)
             ),
    )
    assert sorted(find_cousins(tree, 5)) == [4, 6]
    assert sorted(find_cousins(tree, 2)) == [3]
    assert sorted(find_cousins(tree, 1)) == []


if __name__ == "__main__":
    test_find_cousins()
