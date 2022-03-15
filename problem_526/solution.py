
# This problem was asked by Yahoo.
# 
# You are given a string of length N and a parameter k. The string can be
# manipulated by taking one of the first k letters and moving it to the end.
# 
# Write a program to determine the lexicographically smallest string that can
# be created after an unlimited number of moves.
# 
# For example, suppose we are given the string daily and k = 1. The best we
# can create in this case is ailyd.


def move(word, pos):
    return f"{word[:pos]}{word[pos+1:]}{word[pos]}"


def smallest(word):
    # since out "move" is taking a letter and putting it at the end.
    # with an unlimited number of moves we can just sort the string using 
    # insertion sort.
    for r in range(len(word), 0, -1):
        # find the smallest and move it to the end.
        # we only need to do this for one less letter every time
        smallest_index = 0
        for i, v in enumerate(word[:r]):
            if v < word[smallest_index]:
                smallest_index = i
        word = move(word, smallest_index)
    return word


def test_smallest():
    assert smallest("daily") == "".join(sorted("daily"))


if __name__ == "__main__":
    test_smallest()
