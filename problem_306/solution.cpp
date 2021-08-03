#include <assert.h>

#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

/*
This problem was asked by Palantir.

You are given a list of N numbers, in which each number is located at most k
places away from its sorted position. For example, if k = 1, a given element
at index 4 might end up at indices 3, 4, or 5.

Come up with an algorithm that sorts this list in O(N log k) time.
*/

template<typename T>
std::vector<T> MostlySort(const std::vector<T>& mostly_sorted_input, size_t K) {
    // Since we know that every element is at most K positions from its final
    // location, we can process this in a manner fairly similar to heap sort
    // with our heap constrained to size (K*2 + 1).

    // Put differently, the element whose final location will be i falls within
    // (i-K/2, i+K/2) thus, once we have the element i+K/2 in the heap, we can
    // pop off the top element, O(logK), and guarantee that it will be the
    // correct value.
    std::priority_queue<T, std::vector<T>, std::greater<T>> min_heap;
    std::vector<T> result;

    size_t pos = 0;
    while (pos < mostly_sorted_input.size()) {
        min_heap.push(mostly_sorted_input[pos++]);
        if (pos > K) {
            result.push_back(min_heap.top());
            min_heap.pop();
        }
    }
    while (min_heap.size() > 0) {
        result.push_back(min_heap.top());
        min_heap.pop();
    }

    return result;
}

void TestMostlySort() {
    std::vector<int> example = {1, 0, 2, 5, 3, 4};
    std::vector<int> result = MostlySort(example, 2);
    std::sort(example.begin(), example.end());
    assert(example.size() == result.size());
    for (size_t i = 0; i < example.size(); ++i) {
        assert(example[i] == result[i]);
    }
}

int main() {
    TestMostlySort();
}