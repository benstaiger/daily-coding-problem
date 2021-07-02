import doctest
import unittest
from queue import PriorityQueue



#This problem was asked by Twitter.
#
#A network consists of nodes labeled 0 to N. You are given a list of edges (a, b, t), describing the time t it takes for a message to be sent from node a to node b. Whenever a node receives a message, it immediately passes the message on to a neighboring node, if possible.
#
#Assuming all nodes are connected, determine how long it will take for every node to receive a message that begins at node 0.


def message_prop(N, edges): 
    """
    Find how long it will take to propagate the message to each node.
    Essentially this is a pairwise min path algorithm. Use a modified 
    Dijkstra's to find all min paths.
    """
    # we create a map of all the edges out from each node.
    edge_graph = {s: [] for s in range(N+1)}
    for (s, e, w) in edges:
        edge_graph[s].append((s, e, w))
    distances = [float('inf') for i in range(N+1)]
    distances[0] = 0

    node_queue = PriorityQueue()
    node_queue.put((0, 0))

    while not node_queue.empty():
        w, n = node_queue.get()
        if w == distances[n]:
            for (s2, e2, w2) in edge_graph[n]:
                if distances[n] + w2 < distances[e2]:
                    distances[e2] = distances[n] + w2
                    node_queue.put((distances[n] + w2, e2))

    return max(distances)


def test_message_prop():
    edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (0, 1, 5),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5),
    ]
    assert message_prop(5, edges) == 9


if __name__ == "__main__":
    test_message_prop()
