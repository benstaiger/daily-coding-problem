
# This problem was asked by Microsoft.
# 
# Given an array of numbers and a number k, determine if there are three
# entries in the array which add up to the specified number k. For example,
# given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49.


def sum_of_3(numbers, target):
    numbers = sorted(numbers)  # intentionally not sort in-place

    # simple O(N^2)
    # select the first number, then do a simple two-pointer search
    # for other pairs of number
    for i, v in enumerate(numbers[:-2]):
        start = i + 1
        end = len(numbers) - 1
        while start < end:
            if v + numbers[start] + numbers[end] < target:
                start += 1
            elif v + numbers[start] + numbers[end] > target:
                end -= 1
            else:
                return (v, numbers[start], numbers[end])
    
    return None


def test_sum_of_3():
    numbers = [20, 303, 3, 4, 25]
    target = 49
    print(sum_of_3(numbers, target))


if __name__ == "__main__":
    test_sum_of_3()
