
# This problem was asked by Apple.
# 
# A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:
# 
# if n is even, the next number in the sequence is n / 2
# if n is odd, the next number in the sequence is 3n + 1
# It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.
# 
# Bonus: What input n <= 1000000 gives the longest sequence?


def collatz(n, steps=0):
    assert n > 0
    if n == 1:
        return steps
    if n % 2 == 1:
        return collatz(3 * n + 1) + 1
    else:
        return collatz(n / 2) + 1


def test_seq():
    for i in range(1, 100):
        print(collatz(i))


# To test the longest sequence, we would create a memoized version
# of the sequence with the number of steps


if __name__ == "__main__":
    test_seq()
