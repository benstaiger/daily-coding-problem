
# This problem was asked by Stripe.
# 
# Given an integer n, return the length of the longest consecutive run of 1s
# in its binary representation.
# 
# For example, given 156, you should return 3.


def iter_binary(number):
    if number == 0:
        yield 0
    while number != 0:
        yield (number & 1)
        number = number >> 1


def count_consecutive_ones(number):
    max_run = 0
    run_len = 0
    for n in iter_binary(number):
        if n == 1:
            run_len += 1
        else:
            max_run = max(run_len, max_run)
            run_len = 0
    max_run = max(run_len, max_run)
    return max_run
    

def test_count_consecutive_ones():
    assert count_consecutive_ones(0) == 0
    assert count_consecutive_ones(1) == 1
    assert count_consecutive_ones(2) == 1
    assert count_consecutive_ones(3) == 2
    assert count_consecutive_ones(156) == 3


if __name__ == "__main__":
    test_count_consecutive_ones()
