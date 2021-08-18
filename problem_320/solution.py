
# This problem was asked by Amazon.
# 
# Given a string, find the length of the smallest window that contains every
# distinct character. Characters may appear more than once in the window.
# 
# For example, given "jiujitsu", you should return 5, corresponding to the
# final five letters.


def find_smallest_window(phrase):
    """
    We will find the smallest window with a two-pointer approach. We will start
    by moving the first(end) pointer forward until all values are in the window.
    Then we will push the second(begin) pointer forward until we no longer
    pushing another place forward would no longer cover all values.

    This finds the smallest window possible ending at (end). The we move end
    forward, and start trying to move the begin pointer again.

    As we iterate through this process, we will record the smallest window we
    see. Ultimately, we will find the smallest possible window for each
    possible end point by pushing these two pointers, and thus the global min.

    It will take O(N) time and O(N) space to perform this search.
    """
    counts = {u: 0 for u in phrase}
    num_zero = len(counts)
    min_window = len(phrase)
    begin = 0
    for end, ch_e in enumerate(phrase):
        counts[ch_e] += 1
        if counts[ch_e] == 1:
            num_zero -= 1
        if num_zero == 0:
            while begin < end:
                min_window = min(min_window, end - begin + 1)
                ch_b = phrase[begin]
                if counts[ch_b] == 1:
                    break
                counts[ch_b] -= 1
                begin += 1
    return min_window


def test_find_smallest_window():
    assert find_smallest_window("mississippi") == 9
    assert find_smallest_window("jiujitsu") == 5
    

if __name__ == "__main__":
    test_find_smallest_window()

