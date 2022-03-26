from collections import defaultdict

# This problem was asked by Amazon.
# 
# Given a string, determine whether any permutation of it is a palindrome.
# 
# For example, carrace should return true, since it can be rearranged to form
# racecar, which is a palindrome. daily should return false, since there's no
# rearrangement that can form a palindrome.

def could_be_palindrome(word):
    # Since palindromes are symmetric we know that for an even number of
    # letters in the word, every character must occur an even number of
    # times. If the word has an odd length, then at most one letter can
    # occur an odd number of times and it would be the middle letter.
    letter_count = defaultdict(int)
    for w in word:
        letter_count[w] += 1
    
    num_odd = 0
    for _, v in letter_count.items():
        if v % 2 == 1:
            num_odd += 1
    
    if len(word) % 2 == 0:
        return num_odd == 0
    else:
        return num_odd == 1


def test_palindrome():
    assert could_be_palindrome("carrace")
    assert could_be_palindrome("carrac")
    assert could_be_palindrome("carace") is False


if __name__ == "__main__":
    test_palindrome()
