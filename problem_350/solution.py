from math import sqrt

# This problem was asked by Uber.
# 
# Write a program that determines the smallest number of perfect squares that sum up to N.
# 
# Here are a few examples:
# 
# Given N = 4, return 1 (4)
# Given N = 17, return 2 (16 + 1)
# Given N = 18, return 2 (9 + 9)

# for each value, we can see that N can be done at best N - i**2
# This since for each value, K, less than N we will have to go up to
# sqrt(K) values. our overall runtime is O(N*sqrt(N))


def num_square_sum(N, /):
    if N < 1:
        raise ValueError("Expected parameter >= 1.")

    squares = [i**2 for i in range(int(sqrt(N)) + 1)]
    min_steps = [i for i in range(N+1)]
    for i in range(1, N+1):
        for s in squares:
            if s > i:
                break
            min_steps[i] = min(min_steps[i], min_steps[i - s] + 1)
    return min_steps[-1]

    


def test_num_square_sum():
    assert num_square_sum(4) == 1
    assert num_square_sum(17) == 2
    assert num_square_sum(18) == 2
    assert num_square_sum(19) == 3


if __name__ == "__main__":
    test_num_square_sum()

