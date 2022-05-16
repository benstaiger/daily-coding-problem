#include <cassert>

#include <iostream>
#include <vector>

// This question was asked by Zillow.
// 
// You are given a 2-d matrix where each cell represents number of coins in
// that cell. Assuming we start at matrix[0][0], and can only move right or
// down, find the maximum number of coins you can collect by the bottom right
// corner.
// 
// For example, in this matrix
// 
// 0 3 1 1
// 2 0 0 4
// 1 5 3 1
// The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.

template<typename T>
std::ostream& operator<<(std::ostream& os, const std::vector<T>& data) {
    os << "[";
    for (size_t i = 0; i < data.size(); ++i) {
        os << data[i];
        if (i != data.size() - 1) {
            os << ", ";
        }
    }
    os << "]";
    return os;
}

unsigned best_path(const std::vector<std::vector<unsigned>>& matrix) {
    std::vector<unsigned> prev_best(matrix[0].size(), 0);

    for (const auto& row: matrix) {
        for (int i = 0; i < prev_best.size(); ++i) {
            if (i > 0) {
                prev_best[i] = std::max(prev_best[i], prev_best[i-1]) + row[i];
            } else {
                prev_best[i] = prev_best[i] + row[i];
            }
        }
    }

    return prev_best.back();
}

int main(int argc, char const *argv[]) {
    const std::vector<std::vector<unsigned>> example{{
        {0, 3, 1, 1},
        {2, 0, 0, 4},
        {1, 5, 3, 1}
    }};
    const unsigned res = best_path(example);
    std::cout << res << std::endl;
    return 0;
}
