from math import sqrt

# This problem was asked by PagerDuty.
#
# Given a positive integer N, find the smallest number of steps it will take to
# reach 1.
#
# There are two kinds of permitted steps:
#
# You may decrement N to N - 1.
# If a * b = N, you may decrement N to the larger of a and b.
# For example, given 100, you can reach 1 in five steps with the following
# route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.


# Since the number of steps can be non-decreasing, we need to check all such
# a, b to see if it is the best possible solution.


def large_divisors(N: int):
    """
    Generates all values a, s.t. a * b = N where a >= b
    """
    for i in range(2, int(sqrt(N)) + 1):
        if N % i == 0:
            yield N // i


def test_large_divisors():
    assert list(large_divisors(10)) == [5]
    assert list(large_divisors(9)) == [3]
    assert list(large_divisors(100)) == [50, 25, 20, 10]


def num_steps(N: int):
    if N < 1:
        raise ValueError("N must a positive, non-zero, integer")
    steps = [i-1 for i in range(N+1)]
    for i in range(2, N+1):
        steps[i] = steps[i-1] + 1
        for f in large_divisors(i):
            steps[i] = min(steps[i], steps[f] + 1)
    return steps[N]


def test_num_steps():
    try:
        num_steps(0)
        assert False
    except ValueError:
        pass
    assert num_steps(1) == 0
    assert num_steps(2) == 1
    assert num_steps(3) == 2
    assert num_steps(4) == 2  # 4 -> 2 -> 1
    assert num_steps(5) == 3  # 5 -> 4 -> 2 -> 1
    assert num_steps(11) == 5 # 11 -> 10 ->  9 -> 3 -> 2 -> 1
    assert num_steps(12) == 3  # 12 -> 4 ->  2 -> 1
    assert num_steps(100) == 5  # 100 -> 10 -> 9 -> 3 -> 2 -> 1


if __name__ == "__main__":
    test_large_divisors()
    test_num_steps()

