import heapq

# This problem was asked by Google.

# You are given an M by N matrix consisting of booleans that represents a
# board. Each True boolean represents a wall. Each False boolean represents a
# tile you can walk on.
# 
# Given this matrix, a start coordinate, and an end coordinate, return the
# minimum number of steps required to reach the end coordinate from the start.
# If there is no possible path, then return null. You can move up, left, down,
# and right. You cannot move through walls. You cannot wrap around the edges of
# the board.
# 
# For example, given the following board:
# 
# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum
# number of steps required to reach the end is 7, since we would need to go
# through (1, 2) because there is a wall everywhere else on the second row.


def adjacent(board, i, j):
    next = []
    if i - 1 >= 0 and not board[i-1][j]: # up
        next.append((i-1, j))
    if i + 1 < len(board) and not board[i+1][j]: # down
        next.append((i+1, j))
    if j - 1 >= 0 and not board[i][j-1]: # left
        next.append((i, j-1))
    if j + 1 < len(board[i]) and not board[i][j+1]: # right
        next.append((i, j+1))
    return next


def shortest_path(board, start, end):
    # actually, since we just want number of steps, we can use BFS to find
    # the shortest path.
    seen = [[False for _ in row] for row in board]
    sx, sy = start
    seen[sx][sy] = True

    depth = 1
    to_see = adjacent(board, sx, sy)
    for i, j in to_see:
        seen[i][j] = True

    while to_see:
        next_round = []
        while to_see:
            next = to_see.pop()
            if next == end:
                return depth
            nx, ny = next
            adj = adjacent(board, nx, ny)
            for ax, ay in adj:
                if not seen[ax][ay]:
                    seen[ax][ay] = True
                    next_round.append((ax, ay))
        depth += 1
        to_see = next_round
    return None


def test_path():
    example = [
        [False, False, False, False],
        [True, True, False, True],
        [False, False, False, False],
        [False, False, False, False],
    ]
    start = (3, 0)
    end = (0, 0)
    shortest = shortest_path(example, start, end)
    assert shortest == 7


if __name__ == "__main__":
    test_path()
