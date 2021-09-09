# This problem was asked by Stripe.
#
# reduce (also known as fold) is a function that takes in an array, a
# combining function, and an initial value and builds up a result by calling
# the combining function on each element of the array, left to right. For
# example, we can write sum() in terms of reduce:
#
# def add(a, b):
#     return a + b
#
# def sum(lst):
#     return reduce(lst, add, 0)
#
# This should call add on the initial value with the first element of the
# array, and then the result of that with the second element of the array,
# and so on until we reach the end, when we return the sum of the array.
#
# Implement your own version of reduce.


def my_reduce(data, func, initial_value):
    total = initial_value
    for x in data:
        total = func(total, x)
    return total


def test_reduce():
    assert my_reduce(range(5), lambda x, y: x + y, 0) == 10
    assert my_reduce(range(5), lambda x, y: x + y, -1) == 9
    assert my_reduce(range(1, 5), lambda x, y: x * y, 0) == 0
    assert my_reduce(range(1, 5), lambda x, y: x * y, 1) == 24


if __name__ == "__main__":
    test_reduce()
