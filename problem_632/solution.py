
# This problem was asked by Snapchat.
# 
# You are given an array of length N, where each element i represents the
# number of ways we can produce i units of change. For example, [1, 0, 1, 1, 2]
# would indicate that there is only one way to make 0, 2, or 3 units, and two
# ways of making 4 units.
# 
# Given such an array, determine the denominations that must be in use. In the
# case above, for example, there must be coins with value 2, 3, and 4.


def find_denominations(change):
    # If we already know all denomination < i and we cant make i change enough
    # ways, then i must also be a coin.
    # O(N*k), where k is the number of coins
    ways_so_far = [0 for _ in change]
    ways_so_far[0] = 1

    coins = []

    def add_currency(k):
        coins.append(k)

        for i in range(k, len(ways_so_far)):
            if ways_so_far[i - k] > 0:
                ways_so_far[i] += 1

    for i, v in enumerate(change):
        if ways_so_far[i] < v:
            add_currency(i)
    
    return coins


def test_find_denominations():
    print(find_denominations([1, 0, 1, 1, 2]))


if __name__ == "__main__":
    test_find_denominations()
