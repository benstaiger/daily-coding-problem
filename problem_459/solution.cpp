#include <cmath>
#include <iostream>
#include <limits>
#include <vector>

// This problem was asked by Uber.
// 
// Write a program that determines the smallest number of perfect squares that
// sum up to N.
// 
// Here are a few examples:
// 
// Given N = 4, return 1 (4)
// Given N = 17, return 2 (16 + 1)
// Given N = 18, return 2 (9 + 9)

// solve through dynamic programming.
// the best value for N is going to be
// the best way to solve for N - k for all perfect square
// k less than N.

// this will take sum(sqrt(K), K=1 to N) = O(N * sqrt(N))

template<typename T>
std::ostream& operator<<(std::ostream& stream, const std::vector<T>& vec) {
    stream << "(";
    bool first = true;
    for (const auto& t : vec) {
        if (first) {
            stream << t;
            first = false;
        } else {
            stream << ", " << t;
        }
    }
    stream << ")";
    return stream;
}

int NumSquares(int N) {
    if (N < 1) {
        assert(false);
    }
    std::vector<int> best(N+1, std::numeric_limits<int>::max());
    best[0] = 0;
    best[1] = 1;
    for (int i = 2; i <= N; ++i) {
        for (int j = 1; j <= floor(sqrt(i)); ++j) {
            best[i] = std::min(best[i], 1 + best[i-(j*j)]);
        }
    }
    return best[N];
}

int main() {
    std::vector<int> tests {{
        4, 17, 18
    }};
    for (auto t : tests) {
        std::cout << t << " " << NumSquares(t) << std::endl;
    }
}