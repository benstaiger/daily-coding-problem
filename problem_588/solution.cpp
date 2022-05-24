#include <cassert>

#include <stdexcept>
#include <unordered_map>
#include <vector>

// This problem was asked by Facebook.
// 
// You have a large array with most of the elements as zero.
// 
// Use a more space-efficient data structure, SparseArray, that implements the same interface:
// 
// init(arr, size): initialize with the original large array and size.
// set(i, val): updates index at i with val.
// get(i): gets the value at index i.

template<typename T>
class SparseArray {
  public:
    SparseArray(const std::vector<T>& arr, size_t size, const T& none)
    : _data{} 
    , _size{size}
    , _none{none}
    {
        for (size_t i = 0; i < arr.size(); ++i) {
            if (arr[i] != 0) {
                _data[i] = arr[i];
            }
        }
    }

    void set(size_t i, const T& val) {
        if (i >= _size) {
            throw std::invalid_argument("index out of bounds");
        } 
        auto pos = _data.find(i);
        if (val == 0) {
            if (pos != _data.end()) {
                _data.erase(pos);
            }
        } else {
            pos->second = val;
        }
    }

    const T& get(size_t i) const {
        if (i >= _size) {
            throw std::invalid_argument("index out of bounds");
        } 
        auto pos = _data.find(i);
        if (pos != _data.end()) {
            return pos->second;
        } else {
            return _none;
        }
    }

    size_t size() const { return _size; }
  private:
    // If inorder traversal matters, me might want to use a different structure.
    std::unordered_map<size_t, T> _data;
    const size_t _size;
    const T _none;
};

int main(int argc, char const *argv[]) {
    const size_t size = 10;
    SparseArray<int> example{{1, 2, 3, 4, 5, 6, 7}, size, 0};
    example.set(2, 0);
    for (size_t i = 0; i < example.size(); ++i) {
        if (i < 7 && i != 2) {
            assert(example.get(i) == i+1);
        } else {
            assert(example.get(i) == 0);
        }
    }
    try {
        example.set(size, 11);
        assert(false);
    } catch(std::exception e) {}
    try {
        example.get(size);
        assert(false);
    } catch(std::exception e) {}
    return 0;
}
