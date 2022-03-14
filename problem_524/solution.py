# This problem was asked by Amazon.
# 
# Given an array of numbers, find the maximum sum of any contiguous subarray of
# the array.
# 
# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would
# be 137, since we would take elements 42, 14, -5, and 86.
# 
# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would
# not take any elements.
# 
# Do this in O(N) time.

def find_max_sum(arr):
    # Find the array which includes value v that has the greatest total
    # where v is the "last" element included.
    # If the best-so-far before v is negative, there is no point in including it
    left = [0]
    largest = 0
    prev = 0
    for v in arr:
        total_at_v = (prev + v) if prev > 0 else v
        largest = max(largest, total_at_v)
        prev = total_at_v
    return largest
    

def test_find_max_sum():
    arr1 = [34, -50, 42, 14, -5, 86]
    assert find_max_sum(arr1) == 137

    arr2 = [-5, -1, -8, -9]
    assert find_max_sum(arr2) == 0


if __name__ == "__main__":
    test_find_max_sum()
