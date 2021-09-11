from collections import defaultdict
import string

# This problem was asked by Google.
#
# You are given a set of synonyms, such as (big, large) and (eat, consume).
# Using this set, determine if two sentences with the same number of words are
# equivalent.
#
# For example, the following two sentences are equivalent:
#
# "He wants to eat food."
# "He wants to consume food."
# Note that the synonyms (a, b) and (a, c) do not necessarily imply (b, c):
# consider the case of (coach, bus) and (coach, teacher).
#
# Follow-up: what if we can assume that (a, b) and (a, c) do in fact imply
# (b, c)?


def same_sentence(sentence1, sentence2, thesaurus):
    relations = defaultdict(set)
    for a, b in thesaurus:
        relations[a].add(a)
        relations[a].add(b)
        relations[b].add(a)
        relations[b].add(b)

    sentence1 = sentence1.lower()
    sentence2 = sentence2.lower()

    # For the additional exercise, we can simply map all of the words to
    # numbers. If a word has already been seen, we map all new words in the
    # thesaurus to that group.

    # Check spacing, punctuation, and words to ensure that the sentences have
    # identical structure and meaning
    it1 = 0
    it2 = 0
    while it1 < len(sentence1) and it2 < len(sentence2):
        word1 = ""
        word2 = ""
        while sentence1[it1] in string.ascii_letters:
            word1 += sentence1[it1]
            it1 += 1
        while sentence2[it2] in string.ascii_letters:
            word2 += sentence2[it2]
            it2 += 1

        # check that words are synonyms
        if word1 != word2 and word1 not in relations[word2]:
            return False

        # check punctuation
        if sentence1[it1] != sentence2[it2]:
            return False
        it1 += 1
        it2 += 1
    return True


def test_same_sentence_basic():
    assert same_sentence(
        "He wants to eat food.",
        "He wants to consume food.",
        [("big", "large"), ("eat", "consume")],
    )


def test_same_sentence_missing_synonym():
    assert not same_sentence(
        "He wants to eat food.",
        "He wants to consume food.",
        [("big", "large")],
    )


def test_same_sentence_punctuation():
    assert not same_sentence(
        "He wants to eat food.",
        "He wants to consume food!",
        [("big", "large"), ("eat", "consume")],
    )


if __name__ == "__main__":
    test_same_sentence_basic()
    test_same_sentence_missing_synonym()
    test_same_sentence_punctuation()
