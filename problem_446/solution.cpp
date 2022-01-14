#include <bitset>
#include <cstdint>
#include <iostream>

// This problem was asked by Indeed.
// 
// Given a 32-bit positive integer N, determine whether it is a power of four
// in faster than O(log N) time.

// well, if all you care about is asymptotics, we can do it in O(1) just by checking
// all of them since there are only 16 in since our max value is (4)^16-1 for a
// 32-bit unsigned int.

// alternatively, we could check that the binary format is a one-hot with the
// bit in a correct location.


bool powerOf4(uint32_t n) {
    constexpr uint32_t p0 = 1;
    constexpr uint32_t p1 = 1 << 2;
    constexpr uint32_t p2 = 1 << 4;
    constexpr uint32_t p3 = 1 << 6;
    constexpr uint32_t p4 = 1 << 8;
    constexpr uint32_t p5 = 1 << 10;
    constexpr uint32_t p6 = 1 << 12;
    constexpr uint32_t p7 = 1 << 14;
    constexpr uint32_t p8 = 1 << 16;
    constexpr uint32_t p9 = 1 << 18;
    constexpr uint32_t p10 = 1 << 20;
    constexpr uint32_t p11 = 1 << 22;
    constexpr uint32_t p12 = 1 << 24;
    constexpr uint32_t p13 = 1 << 26;
    constexpr uint32_t p14 = 1 << 28;
    constexpr uint32_t p15 = 1 << 30;
    return n == p0 || n == p1 || n == p2 || n == p3 || n == p4 || n == p5
        || n == p6 || n == p7 || n == p8 || n == p9 || n == p10 || n == p11
        || n == p12 || n == p13 || n == p14 || n == p15;
}

bool powerOf4Bit(uint32_t n) {
    std::bitset<sizeof(decltype(n))*8> b(n);  
    bool hasBit = false;
    for (int i = 0; i < b.size(); ++i) {
        if (b[i]) {
            // if the bit is in the wrong position or we have more than 1.
            if (i % 2 == 1 || hasBit) {
                return false;
            }
            hasBit = true;
        }
    }
    return hasBit;
}

int main() {
    for (uint32_t i = 0; i <= (4*4*4); ++i) {
        std::bitset<32> b(i);
        std::cout << b.to_string() << " " << powerOf4(i) << powerOf4Bit(i) << std::endl;
    }
}