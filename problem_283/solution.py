# This problem was asked by Google.
#
# A regular number in mathematics is defined as one which evenly divides some
# power of 60. Equivalently, we can say that a regular number is one whose
# only prime divisors are 2, 3, and 5.
#
# These numbers have had many applications, from helping ancient Babylonians
# keep time to tuning instruments according to the diatonic scale.
#
# Given an integer N, write a program that returns, in order, the first N
# regular numbers.


def find_regular_numbers(N):
    # for each number in the list, we need to find what is the next possible
    # smallest number. That will be one of our previous numbers
    # multiplied by 2, 3, or 5.
    # for example, when we are at 6 (2*3) we know that the next possible
    # number multiplying by 3 is 9 (3*3) and the next possible when multiplying
    # by 5 is 10 (2*5). and after we reach 10, the next possible smallest
    # when multiplying by 5 will be 15 (3*5) because 3 was the next number
    # after 2 in our sequence so far.
    # We will construct this sequence by keeping an index to the next possible
    # number that we would multiply each divisor by, starting at 1.

    factors = [2, 3, 5]
    regular_numbers = [1]
    indexes = [0 for _ in factors]
    possible = [regular_numbers[i] * f for i, f in zip(indexes, factors)]
    while len(regular_numbers) < N:
        regular_numbers.append(min(possible))
        for idx, p in enumerate(possible):
            # we must look at all possibilities because some might be redundant
            # such as 2*3 and 3*2.
            if p == regular_numbers[-1]:
                indexes[idx] += 1
                possible[idx] = regular_numbers[indexes[idx]] * factors[idx]
    return regular_numbers


def test_find_regular_numbers():
    assert find_regular_numbers(5) == [1, 2, 3, 4, 5]
    assert find_regular_numbers(8) == [1, 2, 3, 4, 5, 6, 8, 9]


if __name__ == "__main__":
    test_find_regular_numbers()
