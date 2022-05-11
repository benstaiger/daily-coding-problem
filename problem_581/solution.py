# This problem was asked by Google.
#
# Given two rectangles on a 2D graph, return the area of their intersection. If
# the rectangles don't intersect, return 0.
#
# For example, given the following rectangles:
#
# {
#     "top_left": (1, 4),
#     "dimensions": (3, 3) # width, height
# }
# and
#
# {
#     "top_left": (0, 5),
#     "dimensions": (4, 3) # width, height
# }
# return 6.


def intersection_area(rect1, rect2):
    x1, y1 = rect1["top_left"]
    w1, h1 = rect1["dimensions"]
    x2, y2 = rect2["top_left"]
    w2, h2 = rect2["dimensions"]

    if x1 < x2:
        xdim = min((x1 + w1) - x2, w2)
    else:
        xdim = min((x2 + w2) - x1, w1)

    if y1 < y2:
        ydim = min((y1 + h1) - y2, h2)
    else:
        ydim = min((y2 + h2) - y1, h1)

    if xdim < 0 or ydim < 0:
        return 0
    return xdim * ydim


def test_intersection():
    rect1 = {"top_left": (1, 4), "dimensions": (3, 3)}
    rect2 = {"top_left": (0, 5), "dimensions": (4, 3)}
    assert intersection_area(rect1, rect2) == 6
    rect1 = {"top_left": (1, 4), "dimensions": (3, 3)}
    rect2 = {"top_left": (1, 4), "dimensions": (2, 2)}
    assert intersection_area(rect1, rect2) == 4


if __name__ == "__main__":
    test_intersection()
