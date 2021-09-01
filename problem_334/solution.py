# This problem was asked by Twitter.
#
# The 24 game is played as follows. You are given a list of four integers,
# each between 1 and 9, in a fixed order. By placing the operators +, -, *, and
# / between the numbers, and grouping them with parentheses, determine whether
# it is possible to reach the value 24.
#
# For example, given the input [5, 2, 7, 8], you should return True, since
# (5 * 2 - 7) * 8 = 24.


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def ways(nums, ops=[add, sub, mul, div]):
    if len(nums) == 1:
        return [(nums[0], str(nums[0]))]

    options = []
    for i in range(1, len(nums)):
        left = ways(nums[:i])
        right = ways(nums[i:])
        for l, l_exp in left:
            for r, r_exp in right:
                for op in ops:
                    try:
                        options.append((op(l, r), f"{op.__name__}({l_exp}, {r_exp})"))
                    except:
                        pass
    return options


def find_24(nums):
    if len(nums) != 4 or not all([i >= 1 and i <= 9 for i in nums]):
        raise ValueError("Expected 4 numbers in [1, 9]")
    for w, exp in ways(nums):
        if w == 24:
            return exp


def test_find_24_given():
    assert eval(find_24([5, 2, 7, 8])) == 24
    print(find_24([5, 2, 7, 8]))


def test_find_24_no_answer():
    assert find_24([1] * 4) is None


if __name__ == "__main__":
    test_find_24_given()
    test_find_24_no_answer()

