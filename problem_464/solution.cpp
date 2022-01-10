#include <algorithm>
#include <iostream>
#include <vector>

// This problem was asked by Google.
// 
// Given a set of distinct positive integers, find the largest subset such that
// every pair of elements in the subset (i, j) satisfies either i % j = 0 or
// j % i = 0.
// 
// For example, given the set [3, 5, 10, 20, 21], you should return
// [5, 10, 20]. Given [1, 3, 6, 24], return [1, 3, 6, 24].


std::vector<unsigned> LargestSubset(const std::vector<unsigned>& inputs) {
    std::vector<unsigned> sizeOfSet(inputs.size(), 1);
    
    for (int i = inputs.size() - 2; i >= 0; --i) {
        // largest subs
        for (int j = i+1; j < inputs.size(); ++j) {
            if (inputs[i] % inputs[j] == 0 || inputs[j] % inputs[i] == 0) {
                // if 6 is divisible by 3, then everything divisible by 6 is also
                // divisible by 3
                sizeOfSet[i] = std::max(sizeOfSet[i], sizeOfSet[j] + 1);
            }
        }
    }

    const auto maxItr = std::max_element(sizeOfSet.begin(), sizeOfSet.end());
    int maxIdx = maxItr - sizeOfSet.begin();

    std::vector<unsigned> result;
    result.push_back(inputs[maxIdx]);
    while (result.size() < *maxItr){
        for (int j = maxIdx+1; j < inputs.size(); ++j) {
            if ((inputs[maxIdx] % inputs[j] == 0 || inputs[j] % inputs[maxIdx] == 0)
                && sizeOfSet[j] + 1 == sizeOfSet[maxIdx]) {
                    result.push_back(inputs[j]);
                    maxIdx = j;
            }
        }
    }
    return sizeOfSet;
}

int main() {
    LargestSubset({{3, 5, 10, 20, 21}});
}