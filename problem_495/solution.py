import random

# This problem was asked by Facebook.
# 
# Given a stream of elements too large to store in memory, pick a random
# element from the stream with uniform probability.

# ... this is literally just asking if you know how to do resevoir sampling


def resevoir_sample(iter):
    selected = next(iter)
    for i,  v in enumerate(iter):
        r = random.randint(0, i+1)
        if r == i:
            selected = v
    return selected
