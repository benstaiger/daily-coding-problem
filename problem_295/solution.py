# This problem was asked by Stitch Fix.
#
# Pascal's triangle is a triangular array of integers constructed with the
# following formula:
#
# The first row consists of the number 1.
# For each subsequent row, each element is the sum of the numbers directly
# above it, on either side.
# For example, here are the first few rows:
#
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
# Given an input k, return the kth row of Pascal's triangle.
#
# Bonus: Can you do this using only O(k) space?


def compute_pascal(level):
    row = [1]
    for _ in range(1, level):
        row.append(0)
        for i in reversed(range(1, len(row))):
            row[i] = row[i - 1] + row[i]
    return row


if __name__ == "__main__":
    for i in range(1, 6):
        print(compute_pascal(i))
