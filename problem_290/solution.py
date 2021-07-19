# This problem was asked by Facebook.
#
# On a mysterious island there are creatures known as Quxes which come in three
# colors: red, green, and blue. One power of the Qux is that if two of them are
# standing next to each other, they can transform into a single creature of the
# third color.
#
# Given N Quxes standing in a line, determine the smallest number of them
# remaining after any possible sequence of such transformations.
#
# For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to
# end up with a single Qux through the following steps:
#
#         Arrangement       |   Change
# ----------------------------------------
# ['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
# ['B', 'B', 'G', 'B']      | (B, G) -> R
# ['B', 'R', 'B']           | (R, B) -> G
# ['B', 'G']                | (B, G) -> R
# ['R']                     |


def qux_fusion(qux1, qux2):
    # Only create the mapping on the first invocation.
    if not hasattr(qux_fusion, "qux_map"):
        bases = {"R", "G", "B"}
        qux_fusion.qux_map = {
            (q1, q2): list(bases - {q1, q2})[0]
            for q1 in bases
            for q2 in bases
            if q1 != q2
        }
    return qux_fusion.qux_map[(qux1, qux2)]


def merge_quxes_greedy(line):
    prev_line = []
    while prev_line != line:
        prev_line = line.copy()
        to_remove = []
        for pos in range(1, len(line)):
            if line[pos - 1] != line[pos]:
                line[pos] = qux_fusion(line[pos - 1], line[pos])
                to_remove.append(pos - 1)
        for pos in reversed(to_remove):
            del line[pos]
    return line


def merge_quxes(arrangement):
    return merge_quxes_greedy(arrangement)


def test_merge_quxes():
    assert merge_quxes(["R", "G", "B", "G", "B"]) != ["R"]


if __name__ == "__main__":
    test_merge_quxes()
