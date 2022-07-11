
# This problem was asked by Pivotal.
# 
# A step word is formed by taking a given word, adding a letter, and
# anagramming the result. For example, starting with the word "APPLE", you can
# add an "A" and anagram to get "APPEAL".
# 
# Given a dictionary of words and an input word, create a function that returns
# all valid step words.


# After an O(N), where N is the number of words, bootstrap. This can actually be
# done in O(1) time with a bag of words look-up in a hashmap.