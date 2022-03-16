
# This problem was asked by Facebook.
# 
# Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0,
# using only mathematical or bit operations. You can assume b can only be 1
# or 0.


def funky_func(x: int, y: int, b: int) -> int:
    assert b in [0, 1]

    mask = b
    # this could be on 32 different lines... but really...
    # of mask | mask << 1 | mask << 2 | ... etc
    for _ in range(31):
        mask = mask | (mask << 1)
    # mask == 0b111..1 or 0b000..0
    # x & mask- return x when mask is all 1 otherwise 0
    # y & ~mask- return y when mask is all 0 otherwise 0
    return x & mask | y & ~mask
    #return  x * b + y * (1 - b)


def test_funky_func():
    assert funky_func(123, 321, 1) == 123
    assert funky_func(123, 321, 0) == 321


if __name__ == "__main__":
    test_funky_func()
