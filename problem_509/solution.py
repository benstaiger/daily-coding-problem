from functools import lru_cache

# This problem was asked by Quora.
# 
# Given a string, find the palindrome that can be made by inserting the fewest
# number of characters as possible anywhere in the word. If there is more than
# one palindrome of minimum length that can be made, return the
# lexicographically earliest one (the first one alphabetically).
# 
# For example, given the string "race", you should return "ecarace", since we
# can add three letters to it (which is the smallest amount to make a
# palindrome). There are seven other palindromes that can be made from "race"
# by adding three letters, but "ecarace" comes first alphabetically.
# 
# As another example, given the string "google", you should return "elgoogle".


def find_palindrome(word):
    # This finds the number...but what about the actual solution...
    # This takes O(N^2) space and time
    @lru_cache(maxsize=None)
    def pal(word):
        if len(word) in [0, 1]:
            return word
        if word[0] == word[-1]:
            return word[0] + pal(word[1:-1]) + word[0]
        else:
            subword1 = pal(word[1:])
            subword2 = pal(word[:-1])
            subword1 = word[0] + subword1 + word[0]
            subword2 = word[-1] + subword2 + word[-1]
            if len(subword1) < len(subword2):
                return subword1
            elif len(subword2) < len(subword1):
                return subword2
            # lexigraphically smallest
            elif subword1 < subword2:
                return subword1
            else:
                return subword2

    return pal(word)
    

def test_find_palindrome():
    assert find_palindrome("race") == "ecarace"
    assert find_palindrome("google") == "elgoogle"


if __name__ == "__main__":
    test_find_palindrome()
