#include <cassert>
#include <cmath>
#include <iostream>

// This problem was asked by Google.
// 
// Implement integer exponentiation. That is, implement the pow(x, y) function,
// where x and y are integers and returns x^y.
// 
// Do this faster than the naive method of repeated multiplication.
// 
// For example, pow(2, 10) should return 1024.

float _pow(float x, int y) {
    // this takes log(y) time and space to evaluate.
    // a real implementation of floating point power is...complicated...
    if (y == 0) return 1;
    if (y == 1) return x;
    if (y % 2 == 0) return pow(x*x, y / 2);
    else return x * pow(x * x, (y-1) / 2);
}

int main() {
    for (int i = 0; i < 10; ++i) {
        assert(pow(2, i) == _pow(2, i));
    }
}
