# This problem was asked by Facebook.
#
# Given a number in Roman numeral format, convert it to decimal.
#
# The values of Roman numerals are as follows:
#
# {
#     'M': 1000,
#     'D': 500,
#     'C': 100,
#     'L': 50,
#     'X': 10,
#     'V': 5,
#     'I': 1
# }
# In addition, note that the Roman numeral system uses subtractive notation for
# numbers such as IV and XL.
#
# For the input XIV, for instance, you should return 14


def translate_from_roman(numeral):
    """
    Translates a string roman numeral to an integer. If the numeral is invalid,
    an exception will be thrown.
    """
    value = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    total = [0]
    prev = value[numeral[-1]]
    for n in reversed(numeral):
        v = value[n]
        if v < prev:
            # start new buffer for subtraction
            total.append(v)
        elif v == prev:
            total[-1] += v
        else:
            # collapse any existing subtraction
            if len(total) > 1:
                v2 = total.pop()
                total[-1] -= v2
            total[-1] += v
        prev = v

    while len(total) > 1:
        v2 = total.pop()
        total[-1] -= v2
    return total[0]


def test_translation():
    assert translate_from_roman("XIV") == 14
    assert translate_from_roman("IV") == 4
    assert translate_from_roman("XL") == 40
    assert translate_from_roman("XII") == 12
    assert translate_from_roman("XXXVI") == 36
    assert translate_from_roman("XIVL") == 36
    assert translate_from_roman("VXL") == 45
    assert translate_from_roman("IVX") == 6
    

if __name__ == "__main__":
    test_translation()
