
# This problem was asked by Square.
# 
# Assume you have access to a function toss_biased() which returns 0 or 1 with
# a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know
# the bias of the coin.
# 
# Write a function to simulate an unbiased coin toss.

def toss_biased():
    pass

def toss_unbiased():
    # If we toss 2 coins, there are 4 outcomes:
    #   H       T 
    # H p*p     p*(1-p)
    # T (1-p)*p (1-p)*(1-p)
    # So we know that the probility of getting HT is the same as TH
    t1 = toss_biased()
    t2 = toss_biased()
    while t1 == t2: 
        t1 = toss_biased()
        t2 = toss_biased()
    # the likelihood of returning decreases as p approaches 0 or 1.
    return t1
