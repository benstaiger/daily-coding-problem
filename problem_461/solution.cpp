#include <vector>

// This problem was asked by Facebook.
// 
// There is an N by M matrix of zeroes. Given N and M, write a function to
// count the number of ways of starting at the top-left corner and getting to
// the bottom-right corner. You can only move right or down.
// 
// For example, given a 2 by 2 matrix, you should return 2, since there are
// two ways to get to the bottom-right:
// 
// Right, then down
// Down, then right
// Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

// Determine the number of paths through an NxM matrix
int numPaths(int N, int M) {
    std::vector<int> numWays(M, 1);

    // The first row will always be 1, 1, 1, ...
    for (int i = 1; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (j >= 1) {
                numWays[j] += numWays[j-1];
            }
        }
    }
    return numWays.back();
}


int main() {
    assert(numPaths(2, 2) == 2);
    assert(numPaths(5, 5) == 70);
}