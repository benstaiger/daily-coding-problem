from functools import reduce

# This problem was asked by Pivotal.
# 
# Write an algorithm that finds the total number of set bits in all integers
# between 1 and N.


def num_bits(x):
    total = 0
    while x > 0:
        total += x & 1
        x = x >> 1
    return total


def brute_force_bits_set(N):
    return reduce(lambda x, y: x + y, map(num_bits, range(N+1)))


def test_bits():
    assert brute_force_bits_set(0) == 0
    assert brute_force_bits_set(1) == 1
    assert brute_force_bits_set(2) == 2
    assert brute_force_bits_set(3) == 4


if __name__ == "__main__":
    test_bits()
