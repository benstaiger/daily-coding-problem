
# This problem was asked by Zillow.
# 
# Let's define a "sevenish" number to be one which is either a power of 7, or
# the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8,
# 49, and so on. Create an algorithm to find the nth sevenish number.


from tkinter import W


def sevenish(n):
    # current_power = 0
    # sevens = [1]
    # powers = [1]
    # while len(sevens) < n:
    #     current_power += 1
    #     powers.append(7**current_power)
    #     new_sevens = [powers[-1] + s for s in sevens]
    #     sevens += [powers[-1]] + new_sevens
        #  we could instead stop instead of writing the whole list
    # this works iff 7^i > sum(7^k, k in 0..i-1)
    # 2^k = sum(2^i, 0..k-1) + 1
    # 7^i < 7^(i+1)
    # 

    # 1st = 7^k^0 + ... + 7^0^1
    # 2nd = 7^k^0 + ... + 7^1^1 + 7^0^0
    # 3rd = 7^k^0 + ... + 7^1^1 + 7^0^1
    # 4th = 7^k^0 + ... + 7^2^1 + 7^1^0 + 7^0^0
    # 5th = 7^k^0 + ... + 7^2^1 + 7^1^0 + 7^0^1

    # we can use the binary encoding of n to identify the sum
    value = 0
    binary = f"{n:b}"
    for i, v in enumerate(reversed(binary)):
        value += (7**i)*int(v)
    return value


def test_sevenish():
    for i in range(15):
        print(sevenish(i))


if __name__ == "__main__":
    test_sevenish()
