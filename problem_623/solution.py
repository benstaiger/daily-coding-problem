# This problem was asked by Palantir.
#
# Write an algorithm to justify text. Given a sequence of words and an integer
# line length k, return a list of strings which represents each line, fully
# justified.
#
# More specifically, you should have as many words as possible in each line.
# There should be at least one space between each word. Pad extra spaces when
# necessary so that each line has exactly length k. Spaces should be distributed
# as equally as possible, with the extra spaces, if any, distributed starting
# from the left.
#
# If you can only fit one word on a line, then you should pad the right-hand
# side with spaces.
#
# Each word is guaranteed not to be longer than k.
#
# For example, given the list of words ["the", "quick", "brown", "fox",
# "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the
# following:
#
# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly


def justify_line(words, length):
    if len(words) == 1:
        spaces = length - len(words[0])
        return words[0] + " " * spaces

    word_len = sum((len(w) for w in words))
    total_space_len = length - word_len
    num_spaces_each = total_space_len // (len(words) - 1)
    num_spaces_overflow = total_space_len % (len(words) - 1)

    line = [words[0]]
    for i in range(1, len(words)):
        if i <= num_spaces_overflow:
            spaces = num_spaces_each + 1
        else:
            spaces = num_spaces_each
        line.append(" " * spaces)
        line.append(words[i])
    return "".join(line)


def test_justify_line():
    assert justify_line(["the", "quick", "brown"], 15) == "the quick brown"
    assert justify_line(["the", "quick", "brown"], 16) == "the  quick brown"
    assert justify_line(["the", "quick", "brown"], 17) == "the  quick  brown"
    assert justify_line(["fox"], 10) == "fox       "


def justify_text(words, length):
    buffer = []
    lines = []
    current_total = 0
    for w in words:
        if current_total + len(w) > length:
            lines.append(justify_line(buffer, length))
            current_total = 0
            buffer = []
        current_total += len(w) + 1
        buffer.append(w)
    if len(buffer) > 0:
        lines.append(justify_line(buffer, length))
    return lines


def test_justify_text():
    assert justify_text(
        "the quick brown fox jumps over the lazy dog".split(" "), 16
    ) == ["the  quick brown", "fox  jumps  over", "the   lazy   dog"]


if __name__ == "__main__":
    test_justify_line()
    test_justify_text()
