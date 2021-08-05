from string import ascii_uppercase

# This problem was asked by Pivotal.
#
# A step word is formed by taking a given word, adding a letter, and
# anagramming the result. For example, starting with the word "APPLE", you can
# add an "A" and anagram to get "APPEAL".
#
# Given a dictionary of words and an input word, create a function that
# returns all valid step words.


def bag_of_words(word_list):
    word_dict = {}
    for word in word_list:
        chars = tuple(sorted(word))
        try:
            word_dict[chars].append(word)
        except KeyError:
            word_dict[chars] = [word]
    return word_dict


def step_words(word, word_list):
    word_dict = bag_of_words(word_list)
    step_words = []
    for ch in ascii_uppercase:
        chars = tuple(sorted(word + ch))
        try:
            step_words += word_dict[chars]
        except KeyError:
            pass
    return step_words


def test_step_words():
    word_list = ["APPLE", "APPEAL", "PAPELS", "PINEAPPLE"]
    assert("APPEAL" in step_words("APPLE", word_list))
    assert("PAPELS" in step_words("APPLE", word_list))
    assert("PINEAPPLE" not in step_words("APPLE", word_list))


if __name__ == "__main__":
    test_step_words()
