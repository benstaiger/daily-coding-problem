from math import ceil

# This problem was asked by Amazon.
# 
# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
# 
# For example, given the following matrix:
# 
# [[1,  2,  3,  4,  5],
#  [6,  7,  8,  9,  10],
#  [11, 12, 13, 14, 15],
#  [16, 17, 18, 19, 20]]
# You should print out the following:
# 
# 1
# 2
# 3
# 4
# 5
# 10
# 15
# 20
# 19
# 18
# 17
# 16
# 11
# 6
# 7
# 8
# 9
# 14
# 13
# 12

def matrix_square_itr(matrix, layer):
    x0, y0 = (layer, layer)
    len_x = len(matrix)
    len_y = len(matrix[0])
    dist_x = len_x - 2*layer
    dist_y = len_y - 2*layer

    for j in range(0, dist_y):
        yield matrix[x0][y0 + j]
    for i in range(1, dist_x):
        yield matrix[x0 + i][y0 + dist_y - 1]
    for j in range(1, dist_y):
        yield matrix[x0 + dist_x - 1][y0 + dist_y - 1 - j]
    for i in range(1, dist_x - 1):
       yield matrix[x0 + dist_x - 1 - i][y0]


def spiral_itr(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    num_layers = min(ceil(rows / 2.0), ceil(cols / 2.0))
    for layer in range(num_layers):
        yield from matrix_square_itr(matrix, layer)


def test_matrix_square_itr():
    matrix = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]
    # layer 0
    matrix_itr = list(matrix_square_itr(matrix, 0))
    expected = [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6]
    assert len(matrix_itr) == len(expected)
    for v1, v2 in zip(expected, matrix_itr):
        assert v1 == v2

    # layer 1
    matrix_itr = list(matrix_square_itr(matrix, 1))
    expected = [7, 8, 9, 14, 13, 12]
    assert len(matrix_itr) == len(expected)
    for v1, v2 in zip(expected, matrix_itr):
        assert v1 == v2


def test_spiral_itr():
    matrix = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]
    expected = [1, 2, 3, 4, 5,
        10, 15, 20,
        19, 18, 17, 16,
        11, 6,
        7, 8, 9,
        14, 13, 12]

    for v1, v2 in zip(expected, spiral_itr(matrix)):
        assert v1 == v2


if __name__ == "__main__":
    test_matrix_square_itr()
    test_spiral_itr()
