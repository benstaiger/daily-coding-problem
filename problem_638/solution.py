
# This problem was asked by Google.
# 
# Given a string of words delimited by spaces, reverse the words in string. For
# example, given "hello world here", return "here world hello"
# 
# Follow-up: given a mutable string representation, can you perform this
# operation in-place?


def simple_reverse_words(sentence):
    return " ".join(reversed(sentence.split(" ")))


def reverse_subsequence(word, i, j):
    idx = 0
    while i + idx < (j - idx):
        # swap letters
        tmp = word[i + idx]
        word[i + idx] = word[j - idx]
        word[j - idx] = tmp
        idx += 1


def inplace_reverse_word(word):
    reverse_subsequence(word, 0, len(word) - 1)


def inplace_reverse_words(sentence):
    # since strings are immutable in python, we will use a list of characters
    # 1. reverse the whole sequence.
    inplace_reverse_word(sentence)
    # 2. reverse the individual words within the sequence.
    first = 0
    for i, w in enumerate(sentence):
        if w == " ":
            reverse_subsequence(sentence, first, i - 1)
            first = i + 1
    if first < len(sentence):
        reverse_subsequence(sentence, first, len(sentence) - 1)
    return sentence


def test_reverse_word():
    assert simple_reverse_words("hello world here") == "here world hello"
    assert "".join(inplace_reverse_words(list("hello world here"))) == "here world hello"


if __name__ == "__main__":
    test_reverse_word()
