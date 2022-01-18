
# This problem was asked by Yahoo.
# 
# Write an algorithm that computes the reversal of a directed graph. For
# example, if a graph consists of A -> B -> C, it should become
# A <- B <- C.


def reverse_graph(graph):
    # for each node in the graph
    # do dfs to find and reverse all connected nodes.
    rev_graph = {k: [] for k in graph}
    seen = {k: False for k in graph}
    def _dfs(node):
        if not seen[node]:
            seen[node] = True

            # add edges to all other nodes
            for e in graph[node]:
                rev_graph[e].append(node)
                if not seen[node]:
                    _dfs(e)
    
    for node in graph:
        if not seen[node]:
            _dfs(node)

    return rev_graph


def test_reverse_graph():
    # the out-going edges from each node stored in a dict.
    graph = {
        'A' : ['B', 'C'],
        'B' : ['C'],
        'C' : []
    }
    rev_graph = reverse_graph(graph)
    assert len(rev_graph['A']) == 0
    assert sorted(rev_graph['B']) == ['A']
    assert sorted(rev_graph['C']) == ['A', 'B']


if __name__ == "__main__":
    test_reverse_graph()
