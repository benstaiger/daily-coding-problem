from math import sqrt

# This problem was asked by Google.
#
# Given a set of points (x, y) on a 2D cartesian plane, find the two closest
# points. For example, given the points [(1, 1), (-1, -1), (3, 4), (6, 1),
# (-1, -6), (-4, -3)], return [(-1, -1), (1, 1)].


def l2_distance(p1, p2):
    return sqrt(sum([(x1 - x2) ** 2 for x1, x2 in zip(p1, p2)]))


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


def find_closest_points(points, distance=l2_distance):
    def check_boundary(p, bound):
        # This takes O(len(p)) time by a slightly complex argument
        # https://people.csail.mit.edu/indyk/6.838-old/handouts/lec17.pdf
        closest = None
        min_dist = bound
        for i in range(len(p)):
            j = i + 1
            while j < len(p) and (p[j][1] - p[i][1]) < min_dist:
                min_dist = distance(p[i], p[j])
                closest = [p[i], p[j]]
                j += 1
        return closest

    def find_closest_points_helper(x_points):
        if len(x_points) <= 3:
            return find_closest_points_brute(points)

        cut = len(x_points) // 2
        left = x_points[:cut]
        right = x_points[cut:]
        middle = x_points[cut]

        closest_left = find_closest_points_helper(left)
        closest_right = find_closest_points_helper(right)

        closest, dist_bound = min(
            (closest_left, distance(*closest_left)),
            (closest_right, distance(*closest_right)),
            key=lambda x: x[1],
        )

        close_points_x = []
        for i in range(len(x_points)):
            if abs(x_points[i][0] - middle[0]) < dist_bound:
                close_points_x.append(x_points[i])
        close_points_x.sort(key=lambda x: x[1])
        # we could avoid this sort by passing down/up a list of y-sorted points
        # that we would merge-sort as we do the point-finding divide and
        # conquer.

        boundary_points = check_boundary(close_points_x, dist_bound)
        if boundary_points:
            closest = boundary_points
        return closest

    x_sorted = sorted(points, key=lambda x: x[0])
    return find_closest_points_helper(x_sorted)


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
