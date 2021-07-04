import pytest

# This problem was asked by Epic.

# The "look and say" sequence is defined as follows: beginning with the term 1,
# each subsequent term visually describes the digits appearing in the previous
# term. The first few terms are as follows:
#
# 1
# 11
# 21
# 1211
# 111221
# As an example, the fourth term is 1211, since the third term consists of one
# 2 and one 1.
#
# Given an integer N, print the Nth term of this sequence.


def int_to_list(val):
    """
    Takes an integer and returns its digits as a list.
    """
    place = 10
    int_list = []
    while val != 0:
        digit = val % place
        val = val // place
        int_list.append(digit)
    int_list.reverse()
    if len(int_list) == 0:
        int_list.append(0)
    return int_list


def list_to_int(int_list):
    """
    Takes an list of integers and returns its digits as an int.
    """
    place = 1
    final = 0
    for ix, digit in enumerate(reversed(int_list)):
        assert digit >= 0 and digit < 10
        final += 10**(ix) * digit
    return final


def test_int_to_list():
    assert int_to_list(0) == [0]
    assert int_to_list(10) == [1, 0]
    assert int_to_list(1) == [1]
    assert int_to_list(15) == [1, 5]


def test_list_to_int():
    assert list_to_int([0]) == 0
    assert list_to_int([1, 0]) == 10
    assert list_to_int([1]) == 1
    assert list_to_int([1, 0, 5]) == 105


def look_and_say(initial_state, iterations):
    """
    Returns an element of the "look and say" sequence from the provided intial
    state. The term numbers are 1-indexed. Requesting term 1 will return the
    initial state.
    """
    assert iterations > 0
    assert initial_state >= 0
    # we could do this without converting to a list by instead iterating
    # over the digits in a manner similar to that above, but it is the code
    # would look a bit cumbersome. The nicest solution would be to use logic
    # that looked like this, but instead abstract the integer behind a class
    # so that we could iterate over its digits in a nice manner without taking
    # up additional space proportional to its length.
    state = int_to_list(initial_state)
    if iterations == 1:
        return list_to_int(state)

    current_state = state
    next_state = []
    for i in range(2, iterations+1):
        last_val = current_state[0]
        count = 1
        for val in current_state[1:]:
            if val == last_val:
                count += 1
            else:
                next_state = next_state + [count, last_val]
                last_val = val
                count = 1
        next_state = next_state + [count, last_val]
        current_state = next_state
        next_state = []
    return list_to_int(current_state)


def test_trivial_initial_conditions():
    assert look_and_say(1, 1) == 1
    assert look_and_say(1, 2) == 11
    assert look_and_say(1, 3) == 21
    assert look_and_say(1, 4) == 1211
    assert look_and_say(1, 5) == 111221


def test_error_conditions():
    look_and_say(-1, 1)  # we cannot encode negative numbers in the sequence
    look_and_say(1, 0)  # sequence is 1-indexed
    look_and_say(1, -1)


if __name__ == "__main__":
    test_int_to_list()
    test_list_to_int()
    test_trivial_initial_conditions()
    # test_error_conditions()
