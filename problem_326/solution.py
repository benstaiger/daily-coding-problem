from dataclasses import dataclass
from typing import List

# This problem was asked by Netflix.
#
# A Cartesian tree with sequence S is a binary tree defined by the following
# two properties:
#
# It is heap-ordered, so that each parent value is strictly less than that of
# its children.
# An in-order traversal of the tree produces nodes with values that correspond
# exactly to S.
# For example, given the sequence [3, 2, 6, 1, 9], the resulting Cartesian
# tree would be:
#
#       1
#     /   \
#   2       9
#  / \
# 3   6
#
# Given a sequence S, construct the corresponding Cartesian tree.


@dataclass(unsafe_hash=True)
class Tree:
    left: "Tree"
    right: "Tree"
    value: int


def inorder_traversal(tree: Tree):
    if tree.left:
        yield from inorder_traversal(tree.left)
    yield tree.value
    if tree.right:
        yield from inorder_traversal(tree.right)


def test_inorder_traversal():
    test_tree = Tree(
        Tree(Tree(None, None, 3), Tree(None, None, 6), 2),
        Tree(None, None, 9),
        1,
    )
    assert list(inorder_traversal(test_tree)) == [3, 2, 6, 1, 9]


def is_heap(tree: Tree) -> bool:
    res = True

    def test_subtree(subtree):
        return tree.value < subtree.value and is_heap(subtree)

    if tree.left:
        res = res and test_subtree(tree.left)
    if tree.right:
        res = res and test_subtree(tree.right)
    return res


def build_cartesian_tree(sequence: List[int]):
    """
    We will break this problem up into sub-problems. We can easily identify
    when we are iterating from left child -> parent because we are guaranteed
    to be decreasing. When we move to the right child, of a tree we will
    increase in value. When we do this, we will recurse and solve the
    the subproblem of the right tree separately, returning the right subtree
    and where we need to continue in the sequence.
    """

    def build_subtree(
        seq, prev_val=float("-inf"), idx=0, lower_bound=float("-inf")
    ):
        tree = None
        while idx < len(sequence):
            s = seq[idx]
            if s <= lower_bound:
                break
            if s <= prev_val:
                # We finished building the previous tree and are now at a new
                # level.
                idx += 1
                right_tree, idx = build_subtree(seq, s, idx, s)
                tree = Tree(tree, right_tree, s)
            if s > prev_val:
                # We are now working on the right child.
                if tree:  # This tree has no left child
                    right_tree, idx = build_subtree(
                        seq, prev_val, idx, prev_val
                    )
                    tree.right = right_tree
                else:
                    tree = Tree(None, None, s)
                    idx += 1
            prev_val = s
        return tree, idx

    res, _ = build_subtree(sequence)
    return res


def simple_nsquare_solution(sequence: List[int]) -> Tree:
    if sequence:
        min_val = min(sequence)
        min_index = sequence.index(min_val)
        if min_index + 1 < len(sequence):
            return Tree(
                simple_nsquare_solution(sequence[:min_index]),
                simple_nsquare_solution(sequence[min_index + 1 :]),
                min_val,
            )
        else:
            return Tree(
                simple_nsquare_solution(sequence[:min_index]), None, min_val
            )
    else:
        return None


def test_build_cartesian_tree():
    def evaluate_sequence(seq):
        tree = build_cartesian_tree(seq)
        # tree = simple_nsquare_solution(seq)
        print(seq)
        print(tree)
        assert list(inorder_traversal(tree)) == seq
        assert is_heap(tree)

    evaluate_sequence([3, 2, 6, 1, 9])
    evaluate_sequence([5, 4, 3, 2, 1])
    evaluate_sequence([1, 2, 3, 4, 5])


if __name__ == "__main__":
    test_inorder_traversal()
    test_build_cartesian_tree()
