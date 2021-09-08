# This problem was asked by Google.
#
# You are given an N by N matrix of random letters and a dictionary of words.
# Find the maximum number of words that can be packed on the board from the
# given dictionary.
#
# A word is considered to be able to be packed on the board if:
#
# It can be found in the dictionary
# It can be constructed from untaken letters by other words found so far on
# the board
# The letters are adjacent to each other (vertically and horizontally, not
# diagonally).
# Each tile can be visited only once by any word.
#
# For example, given the following dictionary:
#
# { 'eat', 'rain', 'in', 'rat' }
# and matrix:
#
# [['e', 'a', 'n'],
#  ['t', 't', 'i'],
#  ['a', 'r', 'a']]
# Your function should return 3, since we can make the words 'eat', 'in', and
# 'rat' without them touching each other. We could have alternatively made
# 'eat' and 'rain', but that would be incorrect since that's only 2 words.


# This problem takes exponential time to solve, instead I will look for all
# words that are on the board (a subproblem)

class DictNode:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.is_word = False

    def add_word(self, word):
        if word == "" or word is None:
            self.is_word = True
            return

        if word[0] not in self.children:
            self.children[word[0]] = DictNode(word[0])
        self.children[word[0]].add_word(word[1:])

    def word(self):
        pass

    def inorder(self):
        words = [self.value] if self.is_word else []
        words += [
            self.value + suff
            for k in sorted(self.children)
            for suff in self.children[k].inorder()
        ]
        return words


def create_dict_tree(words):
    root = DictNode("")
    for word in words:
        root.add_word(word)
    return root


def test_DictNode():
    words = ["cat", "dogge", "dog", "cat-dogge"]
    for i in range(1, len(words)):
        tree = create_dict_tree(words[:i])
        assert tree.inorder() == sorted(words[:i])


def adjacent(row, col, board):
    if row - 1 >= 0:
        yield board[row - 1][col], (row - 1, col)
    if col - 1 >= 0:
        yield board[row][col - 1], (row, col - 1)
    if row + 1 < len(board):
        yield board[row + 1][col], (row + 1, col)
    if col + 1 < len(board[0]):
        yield board[row][col + 1], (row, col + 1)


def test_adjacent():
    board = [[0 for _ in range(3)] for _ in range(3)]
    assert list(adjacent(0, 0, board)) == [(0, (1, 0)), (0, (0, 1))]
    assert list(adjacent(2, 0, board)) == [(0, (1, 0)), (0, (2, 1))]
    assert list(adjacent(2, 1, board)) == [
        (0, (1, 1)),
        (0, (2, 0)),
        (0, (2, 2)),
    ]
    assert list(adjacent(1, 2, board)) == [
        (0, (0, 2)),
        (0, (1, 1)),
        (0, (2, 2)),
    ]
    assert list(adjacent(1, 1, board)) == [
        (0, (0, 1)),
        (0, (1, 0)),
        (0, (2, 1)),
        (0, (1, 2)),
    ]


def find_all_words(words, board):
    def dfs(
        row, col, tree, prefix="", seen=[[False for c in r] for r in board]
    ):
        if seen[row][col]:
            return set()
        seen[row][col] = True

        found_words = set()
        for v, coord in adjacent(row, col, board):
            if v in tree.children:
                found_words |= dfs(
                    *coord,
                    tree=tree.children[v],
                    prefix=prefix + tree.value,
                    seen=seen,
                )
        if tree.is_word:
            found_words.add(prefix + tree.value)
        return found_words

    words_found = set()
    dict_tree = create_dict_tree(words)
    for r, row in enumerate(board):
        for c, v in enumerate(row):
            if board[r][c] in dict_tree.children:
                new_words = dfs(
                    r,
                    c,
                    tree=dict_tree.children[board[r][c]],
                    seen=[[False for c in r] for r in board],
                )
                words_found |= new_words
    return words_found


def test_find_all_words():
    words = ["eat", "rain", "in", "rat"]
    board = [["e", "i", "n"], ["t", "t", "i"], ["a", "r", "a"]]
    print(find_all_words(words, board))


if __name__ == "__main__":
    test_DictNode()
    test_adjacent()
    test_find_all_words()
