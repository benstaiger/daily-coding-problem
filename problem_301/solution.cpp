
#include <array>
#include <cassert>
#include <iostream>

// This problem was asked by Triplebyte.
//
// Implement a data structure which carries out the following operations
// without resizing the underlying array:
//
// add(value): Add a value to the set of values.
// check(value): Check whether a value is in the set.
// The check method may return occasional false positives (in other words,
// incorrectly identifying an element as part of the set), but should always
// correctly identify a true element.


// There are typically 2 implementations of sets:
// ordered: (balanced binary tree)
//  An ordered set could be implemented as a AVL-Tree / RB-Tree
//  using a similar structure that heaps used when represented as vectors
// hashed: (unordered)
//  A hashed set has better average-case time based on the hash function used

// trivial(bad) hash for testing
template<typename T>
size_t hash(const T& v) {
    return static_cast<size_t>(v);
}

template<typename ValueType, size_t Size>
class LinearProbingSet {
    using SetType = LinearProbingSet<ValueType, Size>;
  // This implements an unordered set using linear-probing.
  public:
    LinearProbingSet() : size_(0) {
        occupied_.fill(false);
    }

    LinearProbingSet(SetType&& rhs)
        : size_(rhs.size_)
        , data_(std::move(rhs.data_))
        , occupied_(std::move(rhs.occupied_)) {}

    LinearProbingSet(const SetType& rhs)
        : size_(rhs.size_)
        , data_(rhs.data_)
        , occupied_(rhs.occupied_) {}

    SetType& operator=(SetType&& rhs) {
        if (this != &rhs) {
            size_ = rhs.size_;
            data_ = std::move(rhs.data_);
            occupied_ = std::move(rhs.occupied_);
        }
        return *this;
    }

    SetType& operator=(const SetType& rhs) {
        if (this != &rhs) {
            size_ = rhs.size_;
            std::copy(rhs.data_.begin(), rhs.data_.end(), data_.begin());
            std::copy(rhs.occupied_.begin(), rhs.occupied_.end(), occupied_.begin());
        }
        return *this;
    }

    size_t size() const { return Size; }

    void add(const ValueType& v) {
        // This will not return false negatives but has a worst case O(N)
        // This is true of all hash-based containters. The "constant" time complexity
        // that we often attribute is only true contingent on the output
        // distribution of our hash function for the average case.
        size_t pos = hash(v) % Size;
        size_t num_checked = 0;
        while (occupied_[pos] && num_checked < Size) {
            if (data_[pos] == v) return;
            pos = (pos + 1) % Size;
            ++num_checked;
        }
        // Throw after finding position because we don't want to throw if we
        // don't actually insert the value.
        if (size_ == Size) {
            throw "Set is full.";
        }
        data_[pos] = v;
        occupied_[pos] = true;
        ++size_;
    }

    bool check(const ValueType& v) const {
        // This will not return false negatives but has a worst case O(N).
        // Again, good performance of all hash-based structured is contingent
        // on having a good hashing algorithm for a given data type.
        size_t pos = hash(v) % Size;
        size_t num_checked = 0;
        while (occupied_[pos] && num_checked < Size) {
            if (data_[pos] == v) return true;
            pos = (pos + 1) % Size;
            ++num_checked;
        }
        return false;
    }

  private:
    size_t size_;
    std::array<ValueType, Size> data_;
    std::array<bool, Size> occupied_;
};
 
void testLinearProbingSet() {
    // Test Normal Behavior
    LinearProbingSet<int, 5> testset;  // unrelated, but one of my favorite palindromes.
    for (size_t i = 0; i < testset.size(); ++i) {
        testset.add(i);
    }
    assert(testset.check(0));
    assert(testset.check(6) == false);
    testset.add(0);  // safe because the value already exists
    try {
        testset.add(10);
    } catch (const char* e) {}

    // Test copy constructor
    LinearProbingSet<int, 5> testset2 = testset;
    assert(testset2.check(0));
    assert(testset2.check(6) == false);
    testset2.add(0);  // safe because the value already exists
    try {
        testset2.add(10);
    } catch (const char* e) {}

    // // Test assignment
    LinearProbingSet<int, 5> testset3;
    testset3 = testset;
    assert(testset3.check(0));
    assert(testset3.check(6) == false);
    testset3.add(0);  // safe because the value already exists
    try {
        testset3.add(10);
    } catch (const char* e) {}

    // // Test move constructor
     LinearProbingSet<int, 5> testset4 = std::move(testset3);
     assert(testset4.check(0));
     assert(testset4.check(6) == false);
     testset4.add(0);  // safe because the value already exists
     try {
         testset4.add(10);
     } catch (const char* e) {}

    // // Test move assignment
    LinearProbingSet<int, 5> testset5;
    testset5 = std::move(testset4);
    assert(testset5.check(0));
    assert(testset5.check(6) == false);
    testset5.add(0);  // safe because the value already exists
    try {
        testset5.add(10);
    } catch (const char* e) {}
}

int main() {
    testLinearProbingSet();
    return 0;
}


// The probabilistic solution to this problem that uses the
// leverages the false positives would actually use a bloom filter.