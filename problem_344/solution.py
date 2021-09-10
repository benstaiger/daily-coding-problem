
# This problem was asked by Adobe.
#
# You are given a tree with an even number of nodes. Consider each connection
# between a parent and child node to be an "edge". You would like to remove
# some of these edges, such that the disconnected subtrees that remain each
# have an even number of nodes.
#
# For example, suppose your input was the following tree:
#
#    1
#   / \ 
#  2   3
#     / \ 
#    4   5
#  / | \
# 6  7  8
# In this case, removing the edge (3, 4) satisfies our requirement.
#
# Write a function that returns the maximum number of edges you can remove
# while still satisfying this requirement.


def max_edge_removal(tree, root):
    """
    Greedily remove every edge given the constraint.

    """
    def tree_size(tree, root):
        size = 1
        sizes = {}
        for t in tree[root]:
            t_size, all_sizes = tree_size(tree, t) 
            size += t_size
            for k, s in all_sizes.items():
                sizes[k] = s
        sizes[root] = size
        return size, sizes

    total, sizes = tree_size(tree, root)
    # when traversing tree, check if each edge can be removed.
    stack = [root]
    edges_removed = 0
    while stack:
        node = stack.pop()
        for e in tree[node]:
            if (sizes[node] - sizes[e]) % 2 == 0:
                # remove edge
                edges_removed += 1
                tree[node].remove(e)
                sizes[node] -= sizes[e]
            stack.append(e)
    return edges_removed


def test_max_edge_removal():
    #    1
    #   / \ 
    #  2   3
    #     / \ 
    #    4   5
    #  / | \
    # 6  7  8
    tree = {
        1: [2, 3],
        2: [],
        3: [4, 5],
        4: [6, 7, 8],
        5: [],
        6: [],
        7: [],
        8: [],
    }
    assert max_edge_removal(tree, 1) == 2


if __name__ == "__main__":
    test_max_edge_removal()

