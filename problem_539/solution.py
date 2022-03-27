
# This problem was asked by Pandora.
# 
# Given an undirected graph, determine if it contains a cycle.


def is_acyclic(graph):
    seen = {v: False for v in graph}
    # Augmented dfs:
    # If we see any node again along a given path, then it is creating a cycle
    def dfs(node, path):
        seen[node] = True
        path.add(node)
        for e in graph[node]:
            if e in path:
                return False
            if not seen[e] and not dfs(e, path):
                return False
        path.remove(node)
        return True
    
    for v in graph:
        if not seen[v]:
            if not dfs(v, set()):
                return False
    return True


def test_is_acyclic():
    cyclic_graph = {
        0: [1, 2],
        1: [2],
        2: [0]
    }
    assert is_acyclic(cyclic_graph) is False

    acyclic_graph = {
        0: [1, 2, 3],
        1: [2],
        2: [3],
        3: [],
    }
    assert is_acyclic(acyclic_graph)


if __name__ == "__main__":
    test_is_acyclic()
