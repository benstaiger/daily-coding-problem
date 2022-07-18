
# This problem was asked by Google.
# 
# Given a string, return the first recurring character in it, or null if there
# is no recurring character.
# 
# For example, given the string "acbbac", return "b". Given the string
# "abcdef", return null.


def find_first_reoccurence(word):
    seen = set()
    for w in word:
        if w not in seen:
            seen.add(w)
        else:
            return w
    return None


def test_find_first():
    assert find_first_reoccurence("acbbac") == "b"


if __name__ == "__main__":
    test_find_first()
