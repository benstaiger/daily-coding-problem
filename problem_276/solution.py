
# This problem was asked by Dropbox.
# 
# Implement an efficient string matching algorithm.
# 
# That is, given a string of length N and a pattern of length k, write a program that searches for the pattern in the string with less than O(N * k) worst-case time complexity.
# 
# If the pattern is found, return the start index of its location. If not, return False.


def kmp_preprocess_table(substring):
    """
    Computes the table that describes recurring patterns in the match
    substring.
    """
    pos = 1
    cnd = 0
    table = [-1 for i in range(len(substring)+1)]
    
    while pos < len(substring):
        if substring[pos] == substring[cnd]:
            table[pos] = table[cnd]
        else:
            table[pos] = cnd
            while cnd >= 0 and substring[pos] != substring[cnd]:
                cnd = table[cnd]
        pos += 1
        cnd += 1
    table[pos] = cnd
    return table


def test_kmp_preprocess_table():
    print(kmp_preprocess_table("ABCDABD"))
    print(kmp_preprocess_table("ABACABABC"))
    print(kmp_preprocess_table("AA"))
    print(kmp_preprocess_table("AB"))


def kmp_string_search(text, substring, table):
    """
    Uses the preprocessing table from the KMP algorithm to find all
    substring matches.
    """
    m = 0
    i = 0
    results = []
    while (m+i) < len(text):
        # check if our current position in each string matches
        if text[m+i] == substring[i]:
            i += 1
            # determine if this is a whole match
            if i == len(substring):
                results.append(m)
            else:
                continue
        # move onto the next attempt to substring match
        m = m + i - table[i]
        i = table[i]
        if i < 0:  # there is no common substring.
            i = 0
    return results


def string_match(text, substring):
    """
    This problem as a whole doesn't have too much merit beyond recognizing
    that you should use KMP. In reality, you would almost never need to
    implement this yourself because most languages that support strings
    will already have a substring match.

    Also KMP actually performs better than the specified complexity at
    O(N + k). I would also critique that the return an int or a bool
    depending on the result is a bad function design.
    """
    table = kmp_preprocess_table(substring)
    matches = kmp_string_search(text, substring, table)
    if len(matches) > 0:
        return matches[0]
    else:
        return False

def test_string_match():
    print(string_match("ABC ABCDAB ABCDABCDABDE", "ABCDABD"))


if __name__ == "__main__":
    test_kmp_preprocess_table()
    test_string_match()
