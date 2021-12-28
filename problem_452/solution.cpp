#include <iostream>
#include <list>

// This problem was asked by Microsoft.
// 
// Let's represent an integer in a linked list format by having each node
// represent a digit in the number. The nodes make up the number in reversed
// order.
// 
// For example, the following linked list:
// 
// 1 -> 2 -> 3 -> 4 -> 5
// is the number 54321.
// 
// Given two linked lists in this format, return their sum in the same linked
// list format.
// 
// For example, given
// 
// 9 -> 9
// 5 -> 2
// return 124 (99 + 25) as:
// 
// 4 -> 2 -> 1

std::list<unsigned> add(const std::list<unsigned>& a, const std::list<unsigned>& b) {
    std::list<unsigned> result;
    unsigned remainder = 0;
    auto a_it = a.cbegin();
    auto b_it = b.cbegin();
    while (a_it != a.cend() && b_it != b.cend()) {
        unsigned res = (*a_it + *b_it + remainder) % 10;
        remainder = (*a_it + *b_it + remainder) / 10;
        result.emplace_back(res);
        ++a_it; ++ b_it;
    }
    while (a_it != a.cend()) {
        unsigned res = (*a_it + remainder) % 10;
        remainder = (*a_it + remainder) / 10;
        result.emplace_back(res);
        ++a_it;
    }
    while (b_it != b.cend()) {
        unsigned res = (*b_it + remainder) % 10;
        remainder = (*b_it + remainder) / 10;
        result.emplace_back(res);
        ++b_it;
    }
    if (remainder > 0) {
        result.emplace_back(remainder);
    }

    return result;
}

int main() {
    const std::list<unsigned>  a{
        9, 9
    };
    const std::list<unsigned>  b{
        5, 2
    };
    const std::list<unsigned>  expected{
        4, 2, 1
    };
    const auto res = add(a, b);
    assert(res.size() == expected.size());
    auto res_it = res.cbegin();
    auto exp_it = expected.cbegin();
    for (; res_it != res.cend(); ++res_it, ++exp_it) {
        std::cout << *res_it << std::endl;
        assert(*res_it == *exp_it);
    }
}