
# This problem was asked by Facebook.
#
# Given an integer n, find the next biggest integer with the same number of
# 1-bits on. For example, given the number 6 (0110 in binary), return 9 (1001).



def find_next_number(N):
    """
    To find the next smallest number, we want to move the smallest bit up one
    place. If it hits another bit, we need to push that as well.
    
    Depending on how you look at this, it would take O(1) time when applied
    to a 32-bit int or O(log(N)) when applied to BigInt, time proportional to
    the number of bits used to represent the value.
    """
    print(N)

    place = 0
    mask = 0x1
    # Find the least significant bit
    while N & mask == 0:
        mask = mask << 1

    N -= mask  # Remove bit from value
    mask = mask << 1

    # Fill next highest unfilled bit
    bits_displaced = 0
    while N & mask != 0:
        N -= mask
        mask = mask << 1
        bits_displaced += 1
    N += mask

    # If we passed over mutiple bits, we can move some toward the beginning.
    # For example 011000 -> 100001 instead of 011000 -> 110000
    while bits_displaced > 0:
        N += 1 << (bits_displaced - 1)
        bits_displaced -= 1
    return N


def find_next_number_brute(N):
    """
    Simply iterate until we find a match
    """
    def number_of_bits(x):
        count = 0
        while x > 0:
            if x & 1 == 1:
                count += 1
            x = x >> 1
        return count
    
    num_bits = number_of_bits(N)
    found_bits = 0
    while found_bits != num_bits:
        N += 1
        found_bits = number_of_bits(N)
    return N


def test_cases(solution):
    assert solution(1) == 2
    assert solution(6) == 9
    assert solution(9) == 10
    assert solution(10) == 12


def test_find_next_number_brute():
    test_cases(find_next_number_brute)


def test_find_next_number():
    test_cases(find_next_number)


if __name__ == "__main__":
    test_find_next_number_brute()
    test_find_next_number()

