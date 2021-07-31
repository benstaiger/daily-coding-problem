# This problem was asked by Uber.
#
# You are given a 2-d matrix where each cell consists of either /, \, or an
# empty space. Write an algorithm that determines into how many regions the
# slashes divide the space.
#
# For example, suppose the input for a three-by-six grid is the following:
#
# \    /
#  \  /
#   \/
# Considering the edges of the matrix as boundaries, this divides the grid
# into three triangles, so you should return 3.


def flood_fill(image, start, character):
    # Use BFS to implement flood fill.
    def adjacent(image, point):
        x, y = point
        points = [
            # (x - 1, y - 1),
            (x, y - 1),
            # (x + 1, y - 1),
            (x - 1, y),
            (x + 1, y),
            # (x - 1, y + 1),
            (x, y + 1),
            # (x + 1, y + 1),
        ]
        return [
            (x0, y0)
            for x0, y0 in points
            if x0 >= 0 and x0 < len(image) and y0 >= 0 and y0 < len(image[0])
        ]

    fill = [start]
    while fill:
        # x, y = fill[-1]
        x, y = fill.pop()
        image[x][y] = character
        for x0, y0 in adjacent(image, (x, y)):
            if image[x0][y0] == " ":
                fill.append((x0, y0))
    return image


def find_sections(image):
    # here we assume that the image is well formatted.
    # It is unclear from the problem statement what a "valid" image might look
    # like if partial walls are possible, this will cover that case, the only
    # thing that this does not cover is if this:
    # \
    #  \
    #   /
    # does not actually partition the space.
    # In that case everytime we encounter a wall we could simply check it
    # locally for continuity, if it is discontinuous, we add the points
    # around it when doing the flood fill.
    #
    # This algorithm will take O(N) time where N is the number of characters
    # in the grid since we only inspect each character once in this outer loop
    # and the BFS will only apply to any square once.
    section_number = 0
    for x, row in enumerate(image):
        for y, val in enumerate(row):
            if val == " ":
                section_number += 1
                flood_fill(image, (x, y), str(section_number))
    return section_number


def test_find_sections():
    image = [["\\", " ", " ", " ", " ", "/"],
             [" ", "\\", " ", " ", "/"," "],
             [" ", " ", "\\", "/", " ", " "]]
    print(find_sections(image))
    print(image)


if __name__ == "__main__":
    test_find_sections()
