
# This problem was asked by Yelp.
# 
# Given a mapping of digits to letters (as in a phone number), and a digit
# string, return all possible letters the number could represent. You can
# assume each valid number in the mapping is a single digit.

digit_map = {
    "1": [],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}

def cartesian_product(list1, list2):
    new_list = []
    for l1 in list1:
        for l2 in list2:
            new_list.append(l1 + l2)
    return new_list

def num_possibilities(digit_str):
    total = None
    for d in digit_str:
        if not total:
            total = digit_map[d]
        else:
            total = cartesian_product(total, digit_map[d])
    return total


def test_num_possibilities():
    assert num_possibilities("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]


if __name__ == "__main__":
    test_num_possibilities()
