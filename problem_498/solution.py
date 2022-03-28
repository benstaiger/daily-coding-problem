import bisect
from gettext import find
from os import unsetenv

# This problem was asked by WhatsApp.
#
# Given an array of integers out of order, determine the bounds of the smallest
# window that must be sorted in order for the entire array to be sorted. For
# example, given [3, 7, 5, 6, 9], you should return (1, 3).

def printUnsorted(arr):
    n = len(arr)
    e = n-1
    # step 1(a) of above algo
    for s in range(0,n-1):
        if arr[s] > arr[s+1]:
            break
         
    if s == n-1:
        print ("The complete array is sorted")
        exit()
 
    # step 1(b) of above algo
    e= n-1
    while e > 0:
        if arr[e] < arr[e-1]:
            break
        e -= 1
    print("\t", s, e)
 
    # step 2(a) of above algo
    max = arr[s]
    min = arr[s]
    for i in range(s+1,e+1):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
             
    # step 2(b) of above algo
    for i in range(s):
        if arr[i] > min:
            s = i
            break
 
    # step 2(c) of above algo
    i = n-1
    while i >= e+1:
        if arr[i] < max:
            e = i
            break
        i -= 1
    return s, e


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
