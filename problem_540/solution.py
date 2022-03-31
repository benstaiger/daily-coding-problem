
# This problem was asked by Morgan Stanley.
# 
# In Ancient Greece, it was common to write text with the first line going left
# to right, the second line going right to left, and continuing to go back and
# forth. This style was called "boustrophedon".
# 
# Given a binary tree, write an algorithm to print the nodes in boustrophedon
# order.
# 
# For example, given the following tree:
# 
#        1
#     /     \
#   2         3
#  / \       / \
# 4   5     6   7
# You should return [1, 3, 2, 4, 5, 6, 7].


class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def boustrophedon_order(tree):
    # Do a BFS and alternate insertion into a deque
    layer = [tree]
    forward = True
    output = []

    while layer:
        next_layer = []
        for t in reversed(layer):
            output.append(t.value)
            if forward:
                if t.left:
                    next_layer.append(t.left)
                if t.right:
                    next_layer.append(t.right)
            else:
                if t.right:
                    next_layer.append(t.right)
                if t.left:
                    next_layer.append(t.left)
        layer = next_layer
        forward = not forward
    return output


def test():
    #        1
    #     /     \
    #   2         3
    #  / \       / \
    # 4   5     6   7
    # You should return [1, 3, 2, 4, 5, 6, 7].

    tree = Tree(
        1,
        Tree(
            2,
            Tree(4),
            Tree(5)
        ),
        Tree(
            3,
            Tree(6),
            Tree(7)
        )
    )
    ordered = boustrophedon_order(tree)
    print(ordered)
    expected = [1, 3, 2, 4, 5, 6, 7]
    print(expected)
    assert ordered == expected


if __name__ == "__main__":
    test()
