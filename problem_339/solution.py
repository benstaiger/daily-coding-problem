# This problem was asked by Microsoft.
#
# Given an array of numbers and a number k, determine if there are three
# entries in the array which add up to the specified number k. For example,
# given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49.


def find_sum_3(numbers, total):
    """
    For each value in numbers, we will try to solve the 2 value subproblem
    for total - value. This will take O(N^2) time.
    """
    numbers = sorted(numbers)

    def find_sum_2(nums, t):
        """
        Use 2-pointer method to find the sum
        """
        p1 = 0
        p2 = len(nums) - 1
        while p1 < p2:
            if nums[p1] + nums[p2] > t:
                p2 -= 1
            elif nums[p1] + nums[p2] < t:
                p1 += 1
            else:
                return True

    for i, n in enumerate(numbers):
        if find_sum_2(numbers[:i] + numbers[i + 1 :], total - n):
            return True
    return False


def test_find_sum_3():
    assert find_sum_3([20, 303, 3, 4, 25], 49)


if __name__ == "__main__":
    test_find_sum_3()
