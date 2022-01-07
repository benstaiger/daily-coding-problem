#include <iostream>
#include <tuple>
#include <vector>

// This problem was asked by Alibaba.
// 
// Given an even number (greater than 2), return two prime numbers whose sum
// will be equal to the given number.
// 
// A solution will always exist. See Goldbach’s conjecture.
// 
// Example:
// 
// Input: 4
// Output: 2 + 2 = 4
// If there are more than one solution possible, return the lexicographically
// smaller solution.
// 
// If [a, b] is one solution with a <= b, and [c, d] is another solution with
// c <= d, then
// 
// [a, b] < [c, d]
// If a < c OR a==c AND b < d.

std::pair<int, int> findPrimeSum(int N, const std::vector<int>& primes) {
    assert(N > 2);

    int backItr = primes.size()-1;
    int i = 0;
    for (int i = 0; primes[i] <= (N/2); ++i) {
        const int remainder = N - primes[i];
        while(primes[backItr] > remainder) --backItr;
        if (primes[backItr] == remainder) break;
    }
    // since we always identify the first a that is valid, a < b, it is always
    // the lexigraphically smallest solution.
    return {primes[i], primes[backItr]};
}

int main() {
    // We could write a function to find these or it could be a look-up
    // It doesn't make sense to identify the primes in-line in our function.
    std::vector<int> primes{{
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97
    }};
    const auto& [a, b] = findPrimeSum(16, primes);
    std::cout << a << " " <<  b << std::endl;
}