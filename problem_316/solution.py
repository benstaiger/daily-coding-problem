# This problem was asked by Snapchat.
#
# You are given an array of length N, where each element i represents the
# number of ways we can produce i units of change. For example, [1, 0, 1, 1, 2]
# would indicate that there is only one way to make 0, 2, or 3 units, and two
# ways of making 4 units.
#
# Given such an array, determine the denominations that must be in use. In the
# case above, for example, there must be coins with value 2, 3, and 4.


# We know that change[i] must be made up of coins <= i.
# So if our current number of ways to make i change is less than the possible
# ways, we must add i to the current set of change.
#
# You might wonder why it couldnt possibly be some other value less than i, j.
# If we truly needed to add j instead of i, where j < i, when we encountered
# change[j] our current ways would have been short by 1 since the option of
# just returning j was not present. Thus j should have already been in the set
# for any required j < i. Thus we must add i to our denominations.


def find_denominations(change):
    ways = [0 for _ in change]
    ways[0] = 1
    coins = []
    for i, w in enumerate(ways):
        # we count 2, 1 and 1, 2 as different payments using this method.
        if ways[i - c] > 0:
            ways[i] += ways[i - c]
        if ways[i] < change[i]:
            coins.append(i)
            ways[i] += 1
        if ways[i] != change[i]:
            raise ValueError("Change provided is not possible")
        print(ways)
    return coins


def find_denominations2(array):
    coins = set()

    for i, val in enumerate(array[1:], 1):
        if val > 0:
            for coin in coins:
                if array[(i - coin)] > 0 and ((i - coin) not in coins or (i - coin) <= coin):
                    val -= 1
            if val > 0:
                coins.add(i)

    return coins


def test_find_denominations():
    assert find_denominations([1, 0, 1, 1, 2]) == [2, 3, 4]
    # coins [1, 2]
    # [1, 2, 1] vs [1, 1, 2] vs [2, 1, 1]
    print(find_denominations2([1, 1, 2, 2]))
    # print(find_denominations([1, 1, 2, 3, 5]))
    # assert find_denominations([1, 1, 1, 2, 4]) == [1, 2]


if __name__ == "__main__":
    test_find_denominations()
