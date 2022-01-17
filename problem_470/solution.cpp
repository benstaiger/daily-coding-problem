#include <iostream>
#include <optional>
#include <vector>

// This problem was asked by Google.
// 
// Given an array of numbers and an index i, return the index of the nearest
// larger number of the number at index i, where distance is measured in array
// indices.
// 
// For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.
// 
// If two distances to larger numbers are the equal, then return any one of
// them. If the array at i doesn't have a nearest larger integer, then return
// null.
// 
// Follow-up: If you can preprocess the array, can you do this in constant time?

std::optional<int> distanceLarger(const std::vector<int>& data, int index) {
    int shortest = data.size();
    // search left
    for (int i = index; i >= 0; --i) {
        if (data[i] > data[index]) {
            shortest = i;
            break;
        }
    }
    // search right
    for (int j = index; j < data.size(); ++j) {
        if (data[j] > data[index]) {
            if (j < shortest) {
                shortest = j;
            }
            break;
        }
    }
    return (shortest < data.size()) ? std::optional<int>(shortest) : std::nullopt;
}

int main() {
    std::vector<int> test{{4, 1, 3, 5, 6}};
    assert(distanceLarger(test, 0).value() == 3);
    assert(!distanceLarger(test, 4).has_value());
}