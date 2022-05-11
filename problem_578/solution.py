
# This problem was asked by Bloomberg.
# 
# Determine whether there exists a one-to-one character mapping from one string s1 to another s2.
# 
# For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.
# 
# Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.

def find_character_map(s1, s2):
    if len(s1) != len(s2):
        return None
    
    mapping = {}
    seen = set()
    for w1, w2 in zip(s1, s2):
        if w1 not in mapping:
            if w2 not in seen:  # ensure mapping is unique
                mapping[w1] = w2
                seen.add(w2)
            else:
                return None
        elif mapping[w1] != w2:
            return None
    return mapping


def test_mapping():
    assert find_character_map("abc", "bcd") is not None
    assert find_character_map("foo", "bar") is None


if __name__ == "__main__":
    test_mapping()
