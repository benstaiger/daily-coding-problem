from math import sqrt

# This problem was asked by Google.
#
# Given a set of points (x, y) on a 2D cartesian plane, find the two closest
# points. For example, given the points [(1, 1), (-1, -1), (3, 4), (6, 1),
# (-1, -6), (-4, -3)], return [(-1, -1), (1, 1)].



def l2_distance(p1, p2):
    return sqrt(sum([(x1 - x2)**2 for x1, x2 in zip(p1, p2)]))


def find_closest_points(points):
    pass


def find_closest_points_brute(points, distance=l2_distance):
    closest_points = None
    min_dist = float("inf")
    for ix1, p1 in enumerate(points):
        for ix2, p2 in enumerate(points[:ix1]):
            dist = distance(p1, p2)
            if dist < min_dist:
                closest_points = [p1, p2]
                min_dist = dist
    return closest_points


def given_test(impl):
    points = [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]
    assert sorted(impl(points)) == [(-1, -1), (1, 1)]


def test_find_closest_points_brute():
    given_test(find_closest_points_brute)


def test_find_closest_points():
    given_test(find_closest_points)


if __name__ == "__main__":
    test_find_closest_points_brute()
    test_find_closest_points()
