
# This problem was asked by Airbnb.
# 
# Given a list of words, find all pairs of unique indices such that the
# concatenation of the two words is a palindrome.
# 
# For example, given the list ["code", "edoc", "da", "d"], return
# [(0, 1), (1, 0), (2, 3)].


def is_palindrome(word):
    return all([w1 == w2 for w1, w2 in zip(word, reversed(word))])


def test_is_palindrome():
    assert is_palindrome("hanna") is False
    assert is_palindrome("racecar")
    assert is_palindrome("")


def palindrome_pairs(word_list):
    results = []
    for i, w1 in enumerate(word_list):
        for j, w2 in enumerate(word_list):
            if i != j and is_palindrome(w1 + w2):
                results.append((i, j))
    return results


# we could insert all of the words into a word-tree (Trie)
# Then we could iterate each word in reverse through the tree.
# if we can find the word in the tree, it is a potential match leaving us with
# a couple cases:
#   1.) We are at a leaf node. Great! we could a palindrome
#   2.) We only have 1 path to a leaf
#       We have a palindrom if we can reach the leaf maintaining the invariant.
#   3.) We have multiple paths.
#       Essentially still just case 2


def test_palindrome_pairs():
    # For example, given the list ["code", "edoc", "da", "d"], return
    # [(0, 1), (1, 0), (2, 3)].
    example = ["code", "edoc", "da", "d"]
    idxs = palindrome_pairs(example)
    print(idxs)


if __name__ == "__main__":
    test_is_palindrome()
    test_palindrome_pairs()
