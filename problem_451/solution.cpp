#include <array>
#include <cmath>
#include <iostream>

// This problem was asked by Apple.
// 
// Implement the function fib(n), which returns the nth number in the Fibonacci
// sequence, using only O(1) space.

constexpr unsigned long long fib(unsigned idx) {
    // This solution requires O(1) extra space. A recursive solution does not
    // because the size of the stack will grow linearly as we recurse.
    if (idx == 0 || idx == 1) {
        return 1;
    }
    unsigned long long prevprev = 1;
    unsigned long long prev = 1;
    for (unsigned i = 2; i <= idx; ++i) {
        const unsigned long long next = prev + prevprev;
        prevprev = prev;
        prev = next;
    }
    return prev;
}

unsigned long long fibBinets(unsigned idx) {
    // We can't make this constexpr because pow/sqrt aren't constexpr functions.
    // We could write out own, but that seems beyond the scope of this problem.

    // Another solution to the problem is using the closed form
    // solution. But likely not what an interviewer is actually looking for.
    const long double phi = (1 + sqrt(5.0)) / 2.0;
    const long double psi = (1 - sqrt(5.0)) / 2.0;
    return round((pow(phi, idx + 1) - pow(psi, idx + 1)) / sqrt(5.0));
}

int main() {
    const std::array<unsigned long long, 20> results{
        1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
        2584, 4181, 6765
    };
    for (size_t i = 0; i < 20; ++i) {
        std::cout << fib(i) << " " << fibBinets(i) << std::endl;
        assert(fib(i) == results[i]);
        assert(fibBinets(i) == results[i]);
    }
}