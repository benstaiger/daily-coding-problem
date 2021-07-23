import heapq


def shortest_loop(elevations, paths):
    """
    We will use a modified dijkstra's algorithm to find the shortest
    loop.
    """
    adjacency_list = {}
    for n1, n2 in paths.keys():
        if n1 not in adjacency_list:
            adjacency_list[n1] = []
        elev = elevations[n2] - elevations[n1]
        cost = (elev, paths[(n1, n2)])
        adjacency_list[n1].append((cost, n2))

    locs_to_check = adjacency_list[0]
    heapq.heapify(locs_to_check)  # heapq is a min-heap

    # Always try to go downhill first. If we reach a node going downhill but
    # dont find a shorter path through that node we never have to recheck.
    # Otherwise go uphill, but downhills must always follow with more downhill
    # so the first time we reach a node going downhill, we will only ever look
    # at its downhill paths.

    # since every edge can only be uphill or downhill this will have
    # the same runtime as a normal dijkstra. O(E + VlogV)
    while locs_to_check:
        (elev, dist), next_loc = heapq.heappop(locs_to_check)
        if next_loc == 0:
            return dist
        for (elev2, dist2), node2 in adjacency_list[next_loc]:
            # The next node is always closest by total distance
            if (elev >= 0 or elev2 < 0):
                heapq.heappush(locs_to_check, ((elev2, dist + dist2), node2))
    return None


def test_shortest_loop():
    elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
    paths = {
        (0, 1): 10,
        (0, 2): 8,
        (0, 3): 15,
        (1, 3): 12,
        (2, 4): 10,
        (3, 4): 5,
        (3, 0): 17,
        (4, 0): 10,
    }
    assert shortest_loop(elevations, paths) == 28

    elevations = {0: 5, 1: 25, 2: 15, 3: -20, 4: 10}
    paths = {
        (0, 1): 10,
        (0, 2): 8,
        (0, 3): 15,
        (1, 3): 12,
        (2, 4): 10,
        (3, 4): 5,
        (3, 0): 2,
        (4, 0): 10,
    }
    # 0 -> 3 -> 0 is shorter, but doesn't meet the hill constraint.
    assert shortest_loop(elevations, paths) == 28


if __name__ == "__main__":
    test_shortest_loop()
