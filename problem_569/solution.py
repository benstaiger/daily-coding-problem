
# This problem was asked by Facebook.
# 
# Given an array of numbers of length N, find both the minimum and maximum
# using less than 2 * (N - 2) comparisons.

def min_max(vals):
    if len(vals) % 2 == 0:
        if vals[0] > vals[1]:
            smallest = vals[1]
            largest = vals[0]
        else:
            smallest = vals[0]
            largest = vals[1]
        i = 2
    else:
        smallest = vals[0]
        largest = vals[0]
        i = 1
    
    # 3 comparisons per every 2 elements
    while i < len(vals) - 1:
        big, small = (vals[i], vals[i+1]) if vals[i] > vals[i+1] else (vals[i+1], vals[i])
        if big > largest:
            largest = big
        if small < smallest:
            smallest = small
        i += 2
    return smallest, largest
