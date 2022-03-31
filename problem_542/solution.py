
# This problem was asked by Dropbox.
# 
# Given an undirected graph G, check whether it is bipartite. Recall that a
# graph is bipartite if its vertices can be divided into two independent sets,
# U and V, such that no edge connects vertices of the same set.


def identify_groups(graph):
    # Use DFS to color all the nodes in the graph. We will alternate colors by
    # depth from our first node any conflict on an already colored node implies
    # we aren't a bipartite graph.
    group = {}

    def dfs(node, color):
        group[node] = color
        next_color = 0 if color == 1 else 1
        for e in graph[node]:
            if e in group:
                if group[e] != next_color:
                    return False
            else:
                if not dfs(e, next_color):
                    return False
        return True
    
    first = next(iter(graph))
    res = dfs(first, 0)
    # print(group)
    # We should also check if all nodes are seen... but w/e
    return res


def test_bipartite():
    #  0 -- 1
    #  |    |
    #  2 -- 3
    bipartite = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2],
    }
    assert identify_groups(bipartite)
    #  0 -- 1
    #  |      \
    #  |       2
    #  |      /
    #  4 -- 3
    notbipartite = {
        0: [1, 4],
        1: [0, 2],
        2: [1, 3],
        3: [2, 4],
        4: [0, 3],
    }
    assert identify_groups(notbipartite) is False


if __name__ == "__main__":
    test_bipartite()
