#include <cassert>
#include <iostream>
#include <memory>
#include <string>
#include <vector>

// This problem was asked by Amazon.
// 
// Given an integer N, construct all possible binary search trees with N nodes.

struct Tree {
    Tree(std::shared_ptr<Tree> l=nullptr, std::shared_ptr<Tree> r=nullptr) :
        left(l), right(r) {}
    const std::shared_ptr<Tree> left;
    const std::shared_ptr<Tree> right;

    // Terrible and hacky string repr.
    std::string to_string() const {
        std::string str = "(";
        if (left) {
            str += left->to_string();
        }
        str += " , ";
        if (right) {
            str += right->to_string();
        }
        str += ")";
        return str;
    }
};

std::ostream& operator<<(std::ostream& stream, const Tree& t) {
    return stream << t.to_string();
}

std::vector<std::vector<std::shared_ptr<Tree>>> allTrees(unsigned N) {
    assert(N >= 1);
    // For each value N, store all possible trees.
    // we will use a vector of size N+1 for ease of indexing.
    std::vector<std::vector<std::shared_ptr<Tree>>> trees(N+1);
    trees[0].push_back(nullptr);
    trees[1].push_back(std::make_shared<Tree>(nullptr, nullptr));

    // we can partition each tree based on where its root node is in the tree.
    // we will have i nodes to the left and N-1-i nodes to the right.
    // we can then create all pairs from the already known trees of size i and 
    // N-1-i.

    // We will do this procedure all the way up to N.
    for (size_t i = 2; i <= N; ++i) {
        for (size_t j = 0; j < i; ++j) {
            const auto& trees_left = trees[j];
            const auto& trees_right = trees[i-j-1];
            for (const auto& tree_l : trees_left) {
                for (const auto& tree_r : trees_right) {
                    trees[i].push_back(
                        std::make_shared<Tree>(
                            tree_l,
                            tree_r
                        )
                    );
                }
            }
        }
    }

    return trees;
}

int main() {
    const int numTrees = 3;
    const auto trees = allTrees(numTrees);
    for (size_t i = 1; i < trees.size(); ++i) {
        std::cout << i << " : "<< trees[i].size() << std::endl;
        for (const auto& t : trees[i]) {
            std::cout << *t << std::endl;
        }
    }
}