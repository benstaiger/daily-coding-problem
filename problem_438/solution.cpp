#include <numeric>
#include <tuple>
#include <queue>

// This problem was asked by Amazon.
// 
// Implement a stack API using only a heap. A stack implements the following
// methods:
// 
// push(item), which adds an element to the stack
// pop(), which removes and returns the most recently added element (or throws
// an error if there is nothing on the stack)
// Recall that a heap has the following operations:
// 
// push(item), which adds a new key to the heap
// pop(), which removes and returns the max value of the heap

template<typename T>
class Stack {
  public:
    void push(const T& val) {
        if (count == std::numeric_limits<size_t>::max()) {
            throw std::exception();
        }
        _data.push(std::make_pair(++count, val));
    }

    void push(T&& val) {
        if (count == std::numeric_limits<size_t>::max()) {
            throw std::exception();
        }
        _data.push(std::make_pair(++count, val));
    }

    T pop() {
        if (_data.size() == 0) {
            throw std::exception();
        }
        auto [idx, res] = _data.top();
        _data.pop();
        return res;
    }
  private:
    size_t count = 0;
    std::priority_queue<std::pair<int, T>> _data;
};

int main() {
    Stack<int> test;
    test.push(1);
    test.push(2);
    test.push(3);
    test.push(4);
    test.push(7);

    assert(test.pop() == 7);
    assert(test.pop() == 4);
    assert(test.pop() == 3);
    assert(test.pop() == 2);
    assert(test.pop() == 1);
}