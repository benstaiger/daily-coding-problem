#include <bitset>
#include <cassert>
#include <iostream>

// This problem was asked by Oracle.
// 
// We say a number is sparse if there are no adjacent ones in its binary
// representation. For example, 21 (10101) is sparse, but 22 (10110) is not.
// For a given input N, find the smallest sparse number greater than or equal
// to N.
// 
// Do this in faster than O(N log N) time.

// 111
// 1000
// 1001
// 1010

// isSparse takes log(N) time.
bool isSparse(int N) {
    bool lastTrue = false;
    while (N > 0) {
        bool isTrue = (N & 1) > 0;
        if (isTrue && lastTrue) return false;
        lastTrue = isTrue;
        N = N >> 1;
    }
    return true;
}

// worst case scenario, we have to flip all the bits
// if we do this by adding 1, it takes O(N).

unsigned long smallestSparseTrivial(unsigned long N) {
    while (!isSparse(N)) ++N;
    return N;
}

// 11 -> 100
// 111 -> 1000
// 10111 -> 11000 -> 100000
// find the furthest non, sparse point in the sequence and
// zero everything behind it.
// O(logN)
unsigned long smallestSparse(unsigned long N) {
    std::bitset<sizeof(decltype(N))> bits(N);

    // find the point at which we were "dnse" and then no-longer "dense"
    // (011..110) then switch to (10..000)
    // we do this iteratively as we move through the sequence.
    bool wasDense = false;
    for (size_t i = 1; i < bits.size(); ++i) {
        const bool currentlyDense = bits[i] && bits[i-1];
        if (wasDense && !currentlyDense) {
            // flip bits
            const decltype(N) mask = (std::numeric_limits<decltype(N)>::max() << i);
            bits &= mask;
            bits.set(i);
        }
        wasDense = currentlyDense;
        if (currentlyDense && i == (bits.size() - 1)) {
            // this means there is no such number in the representation.
        }
    }
    return bits.to_ulong();
}

int main() {
    assert(isSparse(20));
    assert(isSparse(21));
    assert(!isSparse(7));
    assert(isSparse(8));
    assert(smallestSparse(3) == 4);
    assert(smallestSparse(7) == 8);
    assert(smallestSparse(20) == 20);
    assert(smallestSparse(22) == 32);
    assert(smallestSparse(23) == 32);
}