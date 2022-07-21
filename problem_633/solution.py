
# This problem was asked by Palantir.
# 
# You are given a list of N numbers, in which each number is located at most k
# places away from its sorted position. For example, if k = 1, a given element
# at index 4 might end up at indices 3, 4, or 5.
# 
# Come up with an algorithm that sorts this list in O(N log k) time.


# We can just sort overlapping buckets of size 2*K
# We will have 2*(N/2*K) buckets to sort in O(KlogK) time.
# This will result in O(N/K * K * log K) = O(N*logK)


def mostly_sorted(data, k):
    for i in range(0, len(data), k):
        lower = max(0, i - k) 
        upper = min(len(data), i + k + 1) 
        # is there a nicer way to sort a slice of a list in-place in python?
        data[lower:upper] = sorted(data[lower:upper])
    return data



def test_mostly_sorted():
    ex = [0, 3, 2, 1, 4, 5, 6, 8, 7]
    sorted_ex = mostly_sorted(ex.copy(), 2)
    assert sorted_ex == sorted(ex)


if __name__ == "__main__":
    test_mostly_sorted()
