#include<iostream>
#include<vector>

// This problem was asked by Google.
// 
// Given an array of strictly the characters 'R', 'G', and 'B', segregate the
// values of the array so that all the Rs come first, the Gs come second, and
// the Bs come last. You can only swap elements of the array.
// 
// Do this in linear time and in-place.
// 
// For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should
// become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].


template<typename Itr, typename V>
void pivotSwap(Itr start, Itr end, V val) {
    while (start < end) {
        while (*start > val) {
            ++start;
        }
        while (*end <= val) {
            --end;
        }

        // swap
        auto tmp = *end;
        *end= *start;
        *start = tmp;

        ++start;
        --end;
    }
}

// We will essentiall just run this as two rounds of quicksort
// where the first pivot value will be G and the second pivot value
// will be B.
template<typename Itr>
void colorSort(Itr start, Itr end) {
    pivotSwap(start, end, 'G');
    pivotSwap(start, end, 'B');
}

int main() {
    std::vector<char> test{{
        'G', 'B', 'R', 'R', 'B', 'R', 'G'
    }};
    colorSort(test.begin(), test.end());
    for (const auto a : test) {
        std::cout << a << std::endl;
    }
}