#include <iostream>
#include <limits>
#include <string>
#include <vector>

// This problem was asked by LinkedIn.
// 
// You are given a string consisting of the letters x and y, such as
// xyxxxyxyy. In addition, you have an operation called flip, which changes a
// single x to y or vice versa.
// 
// Determine how many times you would need to apply this operation to ensure
// that all x's come before all y's. In the preceding example, it suffices to
// flip the second and sixth characters, so you should return 2.


// Swap the first y starting at the beginning with the last y, starting at the
// end.
int NumFlips(std::string_view str) {
    std::vector<int> totalX(str.size());
    int total = 0;
    for (size_t i = 0; i < str.size(); ++i) {
        if (str[i] == 'x') {
            ++total;
        }
        totalX[i] = total;
    }

    // find the point all values before i should be x
    // and how many swaps be required for this to be true.
    int minSwaps = std::numeric_limits<int>::max();
    for (size_t i = 0; i <= str.size(); ++i) {
        // y's before point i
        const int swapToX = i == 0 ? 0 : (i - totalX[i-1]);
        // x's after the point i
        const int swapToY = i == str.size() ? 0 : (totalX[str.size() - 1] - totalX[i]);
        minSwaps = std::min(swapToX + swapToY, minSwaps);
    }
    return minSwaps;
}

int main() {
    assert(NumFlips("xyxxxyxyy") == 2);
}