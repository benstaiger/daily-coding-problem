
# This problem was asked by Amazon.
# 
# Given an array and a number k that's smaller than the length of the array,
# rotate the array to the right k elements in-place.


def rotate1(data):
    tmp = data[-1]
    for i in reversed(range(1, len(data))):
        data[i] = data[i-1]
    data[0] = tmp


def rotate_fwd(data, k):
    if k >= len(data):
        raise KeyError("k expected to be less than len(data).")
    
    def gcd(a, b):
        if b == 0:
            return 1
        else:
            return gcd(b, a % b)

    iters = gcd(k, len(data))
    for i in range(iters): 
        new_pos = (i + k) % len(data)
        while new_pos != i:
            tmp = data[new_pos]
            data[new_pos] = data[i]
            data[i] = tmp
            new_pos = (new_pos + k) % len(data)
    return data


def test_rotate_fwd():
    for i in range(7):
        data = list(range(8))
        print(i, rotate_fwd(data, i))


if __name__ == "__main__":
    test_rotate_fwd()
