#include <cassert>
#include <cmath>
#include <iostream>

// Good morning! Here's your coding interview problem for today.
// 
// Given a real number n, find the square root of n. For example, given n = 9,
// return 3.

float _sqrt(float n, int iter=10) {
    // by the newton method, we can find where the function
    // x*x = n is zero, -> f(x) = x*x - n = 0 by using the tangent
    // line at a point x_hat. The tangent line is
    // f'(x_hat) * (x - x_hat) = y - f(x_hat)
    // so then y = 0 =>
    // - f(x_hat) / f'(x_hat) = x - x_hat
    // -f(x_hat) / f'(x_hat) + x_hat = x
    // x_hat - f(x_hat) / f'(x_hat) = x
    float est = 1;
    for (int i = 0; i < iter; ++i) {
        est -= (est * est - n) / (2 * est);
        std::cout << est << std::endl;
    }
    return est;
}

int main() {
    _sqrt(81);
}