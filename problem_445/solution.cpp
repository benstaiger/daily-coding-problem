#include <memory>

// This question was asked by BufferBox.
// 
// Given a binary tree where all nodes are either 0 or 1, prune the tree so
// that subtrees containing all 0s are removed.
// 
// For example, given the following tree:
// 
//    0
//   / \
//  1   0
//     / \
//    1   0
//   / \
//  0   0
// should be pruned to:
// 
//    0
//   / \
//  1   0
//     /
//    1
// We do not remove the tree at the root or its left child because it still has
// a 1 as a descendant.

struct BoolTree {
    bool value;
    std::shared_ptr<BoolTree> right;
    std::shared_ptr<BoolTree> left;
};

// A tree of all 0s will still return the root 0.
void prune(BoolTree& tree) {
    if (tree.left) {
        prune(*tree.left);
        if (!tree.left->value && !tree.left->left && !tree.left->right) {
            tree.left.reset();
        }
    }
    if (tree.right) {
        prune(*tree.right);
        if (!tree.right->value && !tree.right->left && !tree.right->right) {
            tree.right.reset();
        }
    }
}