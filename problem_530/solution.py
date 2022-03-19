
# This problem was asked by Google.
# 
# The edit distance between two strings refers to the minimum number of
# character insertions, deletions, and substitutions required to change one
# string to the other. For example, the edit distance between “kitten” and
# “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”,
# and append a “g”.
# 
# Given two strings, compute the edit distance between them.


def edit_distance(word1, word2):
    deletion = 1
    insertion = 1
    substitution = 1

    score_table = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

    for i in range(len(word1) + 1):
        score_table[i][0] = i * deletion
    for j in range(len(word2) + 1):
        score_table[0][j] = j * insertion

    for i in range(len(word1)):
        for j in range(len(word2)):
            sub_cost = 0 if word1[i] == word2[j] else substitution
            score_table[i+1][j+1] = min(
                score_table[i][j+1] + deletion,  # deletion
                score_table[i+1][j] + insertion,  # insertion
                score_table[i][j] + sub_cost,  # substitution
            )

    return score_table[len(word1)][len(word2)]


def test_edit_distance():
    assert edit_distance("a", "b") == 1
    assert edit_distance("a", "a") ==  0
    assert edit_distance("acat", "cat") == 1
    assert edit_distance("sitting", "kitten") == 3


if __name__ == "__main__":
    test_edit_distance()
