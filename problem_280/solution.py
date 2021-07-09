# This problem was asked by Pandora.
#
# Given an undirected graph, determine if it contains a cycle.


def find_cycle(graph):
    """
    It is easy to determine if a graph has a cycle by traversing the nodes
    in a DFS order. If we encounter a node that we have seen before that isn't
    the previous node we were at, we have identified a cycle.
    """
    seen = [False for n in graph]

    def dfs(node, parent):
        seen[node] = True
        cycle = False
        for e in graph[node]:
            if not seen[e]:
                cycle = cycle or dfs(e, node)
            elif e != parent:
                return True

    for n in graph:
        if not seen[n]:
            cycle_exists = dfs(n, -1)
            if cycle_exists:
                return True
    return False


def test_find_cycle():
    # cycle of 4 nodes
    graph_with_cycle = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3, 4],
        3: [1, 2],
        4: [2],
    }
    assert find_cycle(graph_with_cycle)
    # cycle of 3 nodes
    graph_with_cycle_2 = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3, 4],
        3: [1, 2],
        4: [2],
    }
    assert find_cycle(graph_with_cycle_2)
    # since our graphs are undirected, we will represent this with a link
    # in both adjacency lists
    graph_without_cycle = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0],
        3: [5, 6],
        4: [],
        5: [],
        6: [],
    }
    assert find_cycle(graph_without_cycle) is False


if __name__ == "__main__":
    test_find_cycle()
