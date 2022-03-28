# This problem was asked by Yahoo.
# 
# Recall that a full binary tree is one in which each node is either a leaf
# node, or has two children. Given a binary tree, convert it to a full one by
# removing nodes with only one child.
# 


class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left
    
    def __repr__(self):
        return f"{self.value}: ({self.left}, {self.right})"


def has_single_child(tree):
    return (tree.left is None) ^ (tree.right is None)


def prune(tree):
    if tree.left is None and tree.right is None:
        return tree

    if has_single_child(tree): 
        if tree.left:
            return prune(tree.left)
        if tree.right:
            return prune(tree.right)

    tree.left = prune(tree.left) 
    tree.right = prune(tree.right) 
    return tree


def test_prune():
    # For example, given the following tree:
    # 
    #          0
    #       /     \
    #     1         2
    #   /            \
    # 3                 4
    #   \             /   \
    #     5          6     7
    # You should convert it to:
    # 
    #      0
    #   /     \
    # 5         4
    #         /   \
    #        6     7
    example = \
    Tree(0,
        Tree(1,
            Tree(3, None, Tree(5)),
            None
            ),
        Tree(2,
            None,
            Tree(4, Tree(6), Tree(7))
            )
        )
    print("before:", example)
    print("after:", prune(example))


if __name__ == "__main__":
    test_prune()