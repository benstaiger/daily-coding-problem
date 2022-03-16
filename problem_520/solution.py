
# This problem was asked by LinkedIn.
# 
# You are given a binary tree in a peculiar string representation. Each node
# is written in the form (lr), where l corresponds to the left child and
# corresponds to the right child.
# 
# If either l or r is null, it will be represented as a zero. Otherwise, it
# will be represented by a new (lr) pair.
# 
# Here are a few examples:
# 
# A root node with no children: (00)
# A root node with two children: ((00)(00))
# An unbalanced tree with three consecutive left children: ((((00)0)0)0)
# Given this representation, determine the depth of the tree.


from tkinter import W


def tree_depth(serial):
    # the deepest point is where we have the most unpaired parenthesis.
    count = 0
    peak = 0
    for w in serial:
        if w == "(":
            count += 1
        if w == ")":
            count -= 1
        peak = max(peak, count)
    return peak


def test_tree_depth():
    # A root node with no children:
    tree1 = "(00)"
    assert tree_depth(tree1) == 1
    # A root node with two children:
    tree2 = "((00)(00))"
    assert tree_depth(tree2) == 2
    # An unbalanced tree with three consecutive left children:
    tree3 = "((((00)0)0)0)"
    assert tree_depth(tree3) == 4


if __name__ == "__main__":
    test_tree_depth()
