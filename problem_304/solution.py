from functools import lru_cache

# This problem was asked by Two Sigma.
#
# A knight is placed on a given square on an 8 x 8 chessboard. It is then
# moved randomly several times, where each move is a standard knight move. If
# the knight jumps off the board at any point, however, it is not allowed to
# jump back on.
#
# After k moves, what is the probability that the knight remains on the board?


def on_board(x, y):
    return x >= 0 and x < 8 and y >= 0 and x < 8


def knight_moves(x, y):
    return [
        (x - 2, y - 1),
        (x - 1, y - 2),
        (x + 2, y - 1),
        (x + 1, y - 2),
        (x - 2, y + 1),
        (x - 1, y + 2),
        (x + 2, y + 1),
        (x + 1, y + 2),
    ]


@lru_cache(maxsize=None)  # memoize for dynamic-programming approach
def probability_off_board(x, y, k):
    if k == 0 and on_board(x, y):
        return 0
    if not on_board(x, y):
        return 1

    prob = (
        sum(
            [
                probability_off_board(x0, y0, k - 1)
                for x0, y0 in knight_moves(x, y)
            ]
        )
        / 8
    )
    return prob


def test_knight_positions():
    print(probability_off_board(-1, 0, 0))  # 100% no moves
    print(probability_off_board(0, 0, 0))  # 0% no moves
    print(probability_off_board(0, 0, 1))  # 6 out of 8 off board
    print(probability_off_board(2, 1, 1))  # 2 out of 8 off board
    print(probability_off_board(1, 2, 1))  # 2 out of 8 off board
    print(probability_off_board(0, 0, 2))  # 0.75*1 + 0.125*0.25 + 0.125*0.25


if __name__ == "__main__":
    test_knight_positions()
