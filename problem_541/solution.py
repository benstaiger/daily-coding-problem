import itertools

# This problem was asked by Amazon.
# 
# Run-length encoding is a fast and simple method of encoding strings. The
# basic idea is to represent repeated successive characters as a single count
# and character. For example, the string "AAAABBBCCDAA" would be encoded as
# "4A3B2C1D2A".
# 
# Implement run-length encoding and decoding. You can assume the string to be
# encoded have no digits and consists solely of alphabetic characters. You can
# assume the string to be decoded is valid.


def run_length_encode(sequence):
    current_letter = None
    current_count = 0
    output = []
    for s in sequence:
        if s == current_letter:
            current_count += 1
        else:
            if current_letter:
                output.append(str(current_count))
                output.append(str(current_letter))
            current_letter = s
            current_count = 1
    if current_letter:
        output.append(str(current_count))
        output.append(str(current_letter))
    return "".join(output)


def run_length_decode(sequence):
    output = []
    for i in range(0, len(sequence), 2):
        num = int(sequence[i])
        val = sequence[i+1]
        output.extend([val]*num)
    return "".join(output)


def test_encode():
    example = "AAAABBBCCDAA"
    expected = "4A3B2C1D2A"
    result = run_length_encode(example)
    assert result == expected


def test_decode():
    expected = "AAAABBBCCDAA"
    example = "4A3B2C1D2A"
    result = run_length_decode(example)
    assert result == expected


if __name__ == "__main__":
    test_encode()
    test_decode()
