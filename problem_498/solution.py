import bisect

# This problem was asked by WhatsApp.
#
# Given an array of integers out of order, determine the bounds of the smallest
# window that must be sorted in order for the entire array to be sorted. For
# example, given [3, 7, 5, 6, 9], you should return (1, 3).


def find_unsorted_window(arr):
    assert len(arr) >= 2
    
    # Find the first time the left / right sub array are not sorted
    for start in range(0, len(arr)-1):
        if arr[start] > arr[start+1]:
            break
    # Array is already sorted
    if start == len(arr) - 2 and arr[start] < arr[start+1]:
        return None
    for end in reversed(range(1, len(arr))):
        if arr[end] < arr[end-1]:
            break

    # Expand the unsorted section if it contains values that should be in 
    # the left / right arrays.
    maximum = max(arr[start:end+1])
    minimum = min(arr[start:end+1])
    start = bisect.bisect(arr, minimum, 0, start)
    end = bisect.bisect(arr, maximum, end+1) - 1
    return start, end


def test_unsorted_window():
    bounds = find_unsorted_window([3, 5, 6, 7, 9])
    assert bounds is None
    bounds = find_unsorted_window([3, 7, 5, 6, 9])
    assert bounds == (1, 3)
    bounds = find_unsorted_window([3, 4, 7, 5, 6, 9])
    assert bounds == (2, 4)
    bounds = find_unsorted_window([10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60])
    assert bounds == (3, 8)
    bounds = find_unsorted_window([0, 1, 15, 25, 6, 7, 30, 40, 50])
    assert bounds == (2, 5)


if __name__ == "__main__":
    test_unsorted_window()
