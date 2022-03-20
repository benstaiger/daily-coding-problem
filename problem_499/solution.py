
# This problem was asked by Palantir.
# 
# A typical American-style crossword puzzle grid is an N x N matrix with black
# and white squares, which obeys the following rules:
# 
# 1.) Every white square must be part of an "across" word and a "down" word.
# 2.) No word can be fewer than three letters long.
# 3.) Every white square must be reachable from every other white square.
# 4.) The grid is rotationally symmetric (for example, the colors of the top
# left and bottom right squares must match).
#
# Write a program to determine whether a given matrix qualifies as a crossword grid.


# this performs checks 1 / 2 
from binascii import Incomplete


def flood_fill_check(board):
    across_lens = [[0 for _ in row] for row in board]
    down_lens = [[0 for _ in row] for row in board]

    n_rows = len(board)
    n_cols = len(board[0])
    
    for j in range(n_cols):
        down_lens[0][j] = 1 if board[0][j] else 0
    for i in range(n_rows):
        across_lens[i][0] = 1 if board[i][0] else 0

    for i, row in enumerate(board):
        for j, is_word in enumerate(row):
            if i > 0 and is_word:
                down_lens[i][j] = down_lens[i-1][j] + 1
            if j > 0 and is_word:
                across_lens[i][j] = across_lens[i][j-1] + 1
            if not is_word:
                if i > 0 and down_lens[i-1][j] < 3 and down_lens[i-1][j] != 0:
                    return False, (i-1, j)
                if j > 0 and across_lens[i][j-1] < 3 and across_lens[i][j-1] != 0:
                    return False, (i, j-1)
    
    # check left edge / bottom
    for j in range(n_cols):
        if down_lens[n_rows-1][j] < 3 and board[n_rows-1][j]:
            return False, (n_rows-1, j)

    for i in range(n_rows):
        if across_lens[i][n_cols-1] < 3 and board[i][n_cols-1]:
            return False, (i, n_cols-1)

    return True, None


def test_flood_fill_check():
    correct_board = [
        [True for i in range(5)] for i in range(5)
    ]
    corr, pos = flood_fill_check(correct_board)
    assert corr
    correct_board = [
        [False, False, True, True,  True],
        [False, False, True, True,  True],
        [True,  True,  True, True,  True],
        [True,  True,  True, False, False],
        [True,  True,  True, False, False],
    ]
    corr, pos = flood_fill_check(correct_board)
    assert corr

    incorrect_board = [
        [False, False, True, True, True],
        [True, False, True, True, True],
        [True, True, True, True, True],
        [True, True, True, False, False],
        [True, True, True, False, False],
    ]
    corr, pos = flood_fill_check(incorrect_board)
    assert corr is False

    incorrect_board = [
        [False, False, True, True, True],
        [False, False, True, True, True],
        [True, True, True, True, True],
        [True, True, True, False, True],
        [True, True, True, False, False],
    ]
    corr, pos = flood_fill_check(incorrect_board)
    assert corr is False


def connected(board):
    n_rows = len(board)
    n_cols = len(board[0])

    seen = [
        [False for _ in row] for row in board
    ]
    start = None
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if board[i][j]:
                start = (i, j)
    if start is None:
        return True

    def dfs(i, j):
        seen[i][j] = True
        if i - 1 >= 0 and board[i-1][j] and not seen[i-1][j]:
            dfs(i-1, j)
        if i + 1 < n_rows and board[i+1][j] and not seen[i+1][j]:
            dfs(i+1, j)
        if j - 1 >= 0 and board[i][j-1] and not seen[i][j-1]:
            dfs(i, j-1)
        if j + 1 < n_cols and board[i][j+1] and not seen[i][j+1]:
            dfs(i, j+1)

    dfs(start[0], start[1])
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if board[i][j] and not seen[i][j]:
                return False
    
    return True


def test_connection():
    correct_board = [
        [False, False, True, True, True],
        [True, False, True, True, True],
        [True, True, True, True, True],
        [True, True, True, False, False],
        [True, True, True, False, False],
    ]
    corr = connected(correct_board)
    assert corr

    incorrect_board = [
        [False, False, True, True, True],
        [False, False, True, True, True],
        [True, True, True, True, True],
        [True, True, True, False, False],
        [True, True, True, False, True],
    ]
    corr = connected(incorrect_board)
    assert corr is False


def check_rotation(board):
    n_rows = len(board)
    n_cols = len(board[0])
    assert n_rows == n_cols

    def rotate_index(x, y):
        return n_rows - x - 1, n_cols - y - 1

    rotation = True
    for i, row in enumerate(board):
        for j, _ in enumerate(row):
            ni, nj = rotate_index(i, j)
            if board[ni][nj] != board[i][j]:
                rotation = False
    return rotation
    

def test_rotation():
    correct_board = [
        [False, False, True, True, True],
        [False, False, True, True, True],
        [True, True, True, True, True],
        [True, True, True, False, False],
        [True, True, True, False, False],
    ]
    corr = check_rotation(correct_board)
    assert corr

    incorrect_board = [
        [False, False, True, True, True],
        [False, False, True, True, True],
        [True, True, True, True, True],
        [True, True, True, False, False],
        [True, True, True, False, True],
    ]
    corr = check_rotation(incorrect_board)
    assert corr is False


if __name__ == "__main__":
    test_flood_fill_check()
    test_connection()
    test_rotation()
