#include <algorithm>
#include <iostream>
#include <memory>
#include <vector>

// This problem was asked by Facebook.
// 
// Given a binary tree, return all paths from the root to leaves.
// 
// For example, given the tree:
// 
//    1
//   / \
//  2   3
//     / \
//    4   5
// Return [[1, 2], [1, 3, 4], [1, 3, 5]].

struct Tree {
    Tree(int v, std::shared_ptr<Tree> l, std::shared_ptr<Tree> r)
        : value{v}
        , left(l)
        , right(r)
    {}
    int value;
    std::shared_ptr<Tree> left;
    std::shared_ptr<Tree> right;
};

namespace {

    void paths_helper(const std::shared_ptr<Tree> tree, std::vector<int>& path, std::vector<std::vector<int>>& results) {
        path.push_back(tree->value);
        if (!tree->left && !tree->right) {
            results.push_back(path);  // No option except copying.
        }
        if (tree->left) {
            paths_helper(tree->left, path, results);
        }
        if (tree->right) {
            paths_helper(tree->right, path, results);
        }
        path.pop_back();
    }

}

std::vector<std::vector<int>> paths(std::shared_ptr<Tree> tree) {
    std::vector<int> path{};
    std::vector<std::vector<int>> results{};
    paths_helper(tree, path, results);
    return results;
}

int main(int argc, char const *argv[])
{
    //    1
    //   / \
    //  2   3
    //     / \
    //    4   5
    const auto example = std::make_shared<Tree>(
        1,
        std::make_shared<Tree>(
            2,
            std::shared_ptr<Tree>(),
            std::shared_ptr<Tree>()
        ),
        std::make_shared<Tree>(
            3,
            std::make_shared<Tree>(
                4,
                std::shared_ptr<Tree>(),
                std::shared_ptr<Tree>()
            ),
            std::make_shared<Tree>(
                5,
                std::shared_ptr<Tree>(),
                std::shared_ptr<Tree>()
            )
        )
    );
    const auto res = paths(example);
    for (const auto& path: res) {
        std::cout << "[";
        for (const auto p: path) {
            std::cout << p << ",";
        }
        std::cout << "], ";
    }
    return 0;
}
