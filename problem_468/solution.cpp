#include <iostream>
#include <vector>

// This problem was asked by Facebook.
// 
// Given an N by N matrix, rotate it by 90 degrees clockwise.
// 
// For example, given the following matrix:
// 
// [[1, 2, 3],
//  [4, 5, 6],
//  [7, 8, 9]]
// you should return:
// 
// [[7, 4, 1],
//  [8, 5, 2],
//  [9, 6, 3]]
//
// Follow-up: What if you couldn't use any extra space?

std::vector<std::vector<int>> rotate90(const std::vector<std::vector<int>>& mat) {
    // a 90 clockwise degree rotation is the same thing as a reflection
    // across the middle and a transposition of the matrix.
    std::vector<std::vector<int>> res(mat.size(), std::vector<int>(mat[0].size()));
    int tmp = mat[0][0];

    // swap the values into the new positions in order
    for (int r = 0; r < mat.size(); ++r) {
        for (int c = 0; c < mat[r].size(); ++c) {
            // reflect + transpose
            const int new_col = mat.size() - r - 1;
            const int new_row = c;
            // index transform 
            res[new_row][new_col] = mat[r][c];
        }
    }
    return res;
}

int main() {
    const std::vector<std::vector<int>> test {
        {{1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 0, 1, 2},
        {3, 4, 5, 6}}
    };
    const auto res = rotate90(test);

    const std::vector<std::vector<int>> testExpected {
        {{3, 9, 5, 1},
         {4, 0, 6, 2},
         {5, 1, 7, 3},
         {6, 2, 8, 4}}
    };

    assert(res.size() == testExpected.size());
    assert(res[0].size() == testExpected.size());
    for (int r = 0; r < res.size(); ++r) {
        for (int c = 0; c < res.size(); ++c) {
            assert(res[r][c] == testExpected[r][c]);
        }
    }
}