
# This problem was asked by Indeed.
# 
# Given a 32-bit positive integer N, determine whether it is a power of four in faster than O(log N) time.


def is_power_of_4(number):
    """
    Identify if the number is a power of 4.
    """
    # 4 ** x = 2 ** (2*x)
    # If our number is a power of two whose exponent is
    # a multiple of 2, we will know that our value is a power of 4.
    # for example 2^4 = 16 = 4^2 or 2^6 = 64 = 4^3
     
    # We can manipulate the bits to identify whether or not this is true.
    # A power of 2 will be identifiable in binary as a single bit and its
    # exponent will be denoted by its position.
    # however for a 32-bit unsigned integer, there are only 17 possible
    # powers of 4 (including 0).
    # it is simplest (and likely fastest) to just explicitly check these
    # values.

    # Both of the implementations are constant time solutions.

    return number in [4**i for i in range(16+1)]


def test_is_power_of_4():
    assert is_power_of_4(4**3) is True
    assert is_power_of_4(16) is True
    assert is_power_of_4(4) is True
    assert is_power_of_4(8) is False
    assert is_power_of_4(4**3 - 1) is False


if __name__ == "__main__":
    test_is_power_of_4()
    
