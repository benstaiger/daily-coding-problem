from collections import defaultdict
from re import I

# This problem was asked by Google.
# 
# On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.
# 
# You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).
# 
# For example, given M = 5 and the list of bishops:
# 
# (0, 0)
# (1, 2)
# (2, 2)
# (4, 0)
# The board would look like this:
# 
# [b 0 0 0 0]
# [0 0 b 0 0]
# [0 0 b 0 0]
# [0 0 0 0 0]
# [b 0 0 0 0]
# You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.


# We can do this in O(B) time where B is the number of bishops by hashing them
# into a map based on their diagonal number. The diagonal number is (x - y) so
# the longest diagonal is diagonal 0, the diagonal starting at (1, 0) is 1, etc
# similarly we can find the diagonals going perpendicular by (y - x)
def find_bishop_pairs(bishops):
    diags1 = defaultdict(list)
    diags2 = defaultdict(list)
    for i, (x, y) in enumerate(bishops):
        diags1[x - y].append(i)
        diags2[y - x].append(i)

    def choose_2(N):
        return N * (N-1) / 2

    total_attacks = 0
    for _, group in diags1.items():
        N = len(group)
        if N > 1:
            # N choose 2 different pairs attacking
            total_attacks += choose_2(N)

    # A pair in diags2 CANNOT also be in diags1 unless a bishop is in the list
    # twice.
    for _, group in diags2.items():
        N = len(group)
        if N > 1:
            total_attacks += choose_2(N)

    return total_attacks


def test_bishops():
    example = [
        (0, 0),
        (1, 2),
        (2, 2),
        (4, 0),
    ]
    total = find_bishop_pairs(example)
    assert total == 2


if __name__ == "__main__":
    test_bishops()
