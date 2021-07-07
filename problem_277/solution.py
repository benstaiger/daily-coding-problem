import doctest
from enum import Enum

# This problem was asked by Google.
#
# UTF-8 is a character encoding that maps each symbol to one, two, three, or
# four bytes.
#
# For example, the Euro sign, €, corresponds to the three bytes 11100010
# 10000010 10101100. The rules for mapping characters are as follows:
#
# For a single-byte character, the first bit must be zero.
# For an n-byte character, the first byte starts with n ones and a zero. The
# other n - 1 bytes all start with 10.
# Visually, this can be represented as follows.
#
#  Bytes   |           Byte format
# -----------------------------------------------
#    1     | 0xxxxxxx
#    2     | 110xxxxx 10xxxxxx
#    3     | 1110xxxx 10xxxxxx 10xxxxxx
#    4     | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
#
# Write a program that takes in an array of integers representing byte values,
# and returns whether it is a valid UTF-8 encoding.


def extract_byte(val, position):
    """
    Extracts one of the four bytes from an integer val

    >>> extract_byte(0x01234567, 0) == 0x01
    True
    >>> extract_byte(0x01234567, 1) == 0x23
    True
    >>> extract_byte(0x01234567, 2) == 0x45
    True
    >>> extract_byte(0x01234567, 3) == 0x67
    True
    """
    mask = 0xFF000000 >> (position * 8)
    return (val & mask) >> ((3 - position) * 8)


def read_bytes(ints):
    """
    Takes a list of integers and returns an iterable stream of bytes.
    >>> list(read_bytes([0xAABBCCDD])) == [0xAA, 0xBB, 0xCC, 0xDD]
    True
    >>> list(read_bytes([0xAABBCCDD]*2)) == [0xAA, 0xBB, 0xCC, 0xDD]*2
    True
    """
    for val in ints:
        for position in range(4):
            yield extract_byte(val, position)


class Byte(Enum):
    DATA_BYTE_1 = 0
    DATA_BYTE_MANY = 1
    DATA_HEADER_2 = 2
    DATA_HEADER_3 = 3
    DATA_HEADER_4 = 4
    BAD_SERIALIZATION = 5


def identify_byte(byte):
    """
    Identifies the type of byte in the utf-8 encoding.
    """
    # Maybe these should be constructed instead of hard-coded. It would make
    # things much more understandable.
    if byte & 0xF8 == 0xF8:
        return Byte.BAD_SERIALIZATION
    elif byte & 0xF0 == 0xF0 and byte & 0x08 == 0:
        return Byte.DATA_HEADER_4
    elif byte & 0xE0 == 0xE0 and byte & 0x10 == 0:
        return Byte.DATA_HEADER_3
    elif byte & 0xC0 == 0xC0 and byte & 0x20 == 0:
        return Byte.DATA_HEADER_2
    elif byte & 0x80 == 0x80 and byte & 0x40 == 0:
        return Byte.DATA_BYTE_MANY
    elif byte & 0x80 == 0:
        return Byte.DATA_BYTE_1
    else:
        return Byte.BAD_SERIALIZATION


def test_identify_byte():
    assert identify_byte(0xF6) == Byte.DATA_HEADER_4
    assert identify_byte(0xE6) == Byte.DATA_HEADER_3
    assert identify_byte(0xD6) == Byte.DATA_HEADER_2
    assert identify_byte(0xC6) == Byte.DATA_HEADER_2
    assert identify_byte(0x16) == Byte.DATA_BYTE_1
    assert identify_byte(0xA6) == Byte.DATA_BYTE_MANY
    assert identify_byte(0xFF) == Byte.BAD_SERIALIZATION


def idenitfy_utf8(ints):
    """
    Takes a list of 4-byte integers and determines if it is a valid utf-8
    encoding.

    In reality, there are a lot of things to consider when doing this type of
    analysis such as Endian-ness, the fact that python actually has big-int
    representation if integers are too large etc. We will make some naive
    assumptions for the sake of solving the problem.

    We will construct a finite state machine that will iterate over bytes
    from the sequence to validate the serialization.
    """

    def failure(next_byte):
        return failure

    def waiting_1(next_byte):
        if next_byte == Byte.DATA_BYTE_MANY:
            return waiting
        else:
            return failure

    def waiting_2(next_byte):
        if next_byte == Byte.DATA_BYTE_MANY:
            return waiting_1
        else:
            return failure

    def waiting_3(next_byte):
        if next_byte == Byte.DATA_BYTE_MANY:
            return waiting_2
        else:
            return failure

    def waiting(next_byte):
        if next_byte == Byte.BAD_SERIALIZATION:
            return failure
        if next_byte == Byte.DATA_BYTE_1:
            return waiting
        elif next_byte == Byte.DATA_HEADER_2:
            return waiting_1
        elif next_byte == Byte.DATA_HEADER_3:
            return waiting_2
        elif next_byte == Byte.DATA_HEADER_4:
            return waiting_3

    state = waiting
    for byte in read_bytes(ints):
        next_byte = identify_byte(byte)
        state = state(next_byte)
        if state == failure:
            return False

    if state == waiting:
        return True
    else:
        return False


def test_identify_utf8():
    data_byte = 0b01111111
    many_data_byte = 0b10111111
    header_2_byte = 0b11011111
    header_3_byte = 0b11101111
    header_4_byte = 0b11110111

    # test simple 1-byte characters
    data_int = (
        data_byte + (data_byte << 8) + (data_byte << 16) + (data_byte << 24)
    )
    test_case = [data_int]
    # assert idenitfy_utf8(test_case) is True

    # test multiple-byte character
    header_int = (
        (header_4_byte << 24)
        + (many_data_byte << 16)
        + (many_data_byte << 8)
        + (many_data_byte)
    )
    assert idenitfy_utf8([header_int]) is True

    # test mutiple-byte character with too few data
    header_int_few = (
        (header_4_byte << 24)
        + (many_data_byte << 16)
        + (many_data_byte << 8)
        + (data_byte)
    )
    assert idenitfy_utf8(test_case + [header_int_few]) is False

    # test mutiple-byte character with too many data
    header_int_many = (
        (header_3_byte << 24)
        + (many_data_byte << 16)
        + (many_data_byte << 8)
        + (many_data_byte)
    )
    assert idenitfy_utf8(test_case + [header_int_many]) is False

    # test wrapping across ints
    header_int_1 = (
        (data_byte << 24)
        + (data_byte << 16)
        + (header_3_byte << 8)
        + (many_data_byte)
    )
    header_int_2 = (
        (many_data_byte << 24)
        + (data_byte << 16)
        + (data_byte << 8)
        + (data_byte)
    )
    assert idenitfy_utf8(test_case + [header_int_1, header_int_2]) is True


if __name__ == "__main__":
    doctest.testmod()
    test_identify_byte()
    test_identify_utf8()
