
# This problem was asked by Microsoft.
# 
# Given a string and a pattern, find the starting indices of all occurrences of
# the pattern in the string. For example, given the string "abracadabra" and
# the pattern "abr", you should return [0, 7].

# So... implement KMP.


def kmp_reset(pattern):
    reset = [-1 for _ in range(len(pattern) + 1)]

    pos = 1
    suff = 0

    # At position, pos, how much upto and including pos is a prefix of the
    # pattern
    while pos < len(pattern):
        if pattern[pos] == pattern[suff]:
            reset[pos] = reset[suff]
        else:
            reset[pos] = suff
            while suff >= 0 and pattern[pos] != pattern[suff]:
                suff = reset[suff]
        pos += 1
        suff += 1
    reset[pos] = suff
    return reset
        
    


def kmp_match(word, pattern):
    # iterate through the word a single time. if we ever meet a letter
    # that does not match our current position in the pattern, we use the
    # reset table to see if the suffix of our partial match is a prefix of
    # the string. (AKA if part of the match could actually be reused)
    matches = []
    reset = kmp_reset(pattern)

    i = 0
    p_idx = 0
    while i < len(word):
        if word[p_idx] == word[i]:
            p_idx += 1
            i += 1
            if p_idx == len(pattern):
                matches.append(i - p_idx)
                p_idx = reset[p_idx]
        else:
            p_idx = reset[p_idx]
            if p_idx < 0:
                p_idx = 1
                i += 1 
    return matches


def test_kmp_match():
    idx = kmp_match("abracadabra", "abra")
    print(idx)
    assert idx == [0, 7]


if __name__ == "__main__":
    test_kmp_match()