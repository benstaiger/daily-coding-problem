import random

# This problem was asked by Facebook.
#
# Given a function that generates perfectly random numbers between 1 and k
# (inclusive), where k is an input, write a function that shuffles a deck of
# cards represented as an array using only swaps.
#
# It should run in O(N) time.
#
# Hint: Make sure each one of the 52! permutations of the deck is equally likely.


def fisher_yates_shuffle(data):
    for i in range(len(data) - 1, -1, 0):
        j = random.randrange(0, i+1)
        data[j], data[i] = data[i], data[j]
    return data

# Fisher-Yates proof of uniform shuffle:
#   1.) The probability that any element is in the last position (the first swap)
#   is 1/n since we do a random swap with uniform probability.
#   2.) The probability that any element is in the second to the last position
#   falls into two cases:
#       1.) it was not chosen in the first case and was then chosen w/ prob 1/(n-1)
#           = ((n-1)/n)) * (1/(n-1)) = 1/n
#       2.) it was the last element = (prob last was not chosen in first iter) * (prob chosen)
#           = ((n-1)/n) * (1/(n-1)) = 1/n
#   We could continue this pattern for all 52 positions.