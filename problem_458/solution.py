from collections import defaultdict
from typing import DefaultDict

# This problem was asked by Uber.
# 
# A rule looks like this:
# 
# A NE B
# 
# This means this means point A is located northeast of point B.
# 
# A SW C
# 
# means that point A is southwest of C.
# 
# Given a list of rules, check if the sum of the rules validate. For example:
# 
# A N B
# B NE C
# C N A
# does not validate, since A cannot be both north and south of C.
# 
# A NW B
# A N B
# is considered valid.

# For a given direction, we can create a DAG that implies the relationship
# in the given direction. As long as it doesn't have any cycles. It is a valid
# relationship. We can evaluate if there are cycles through DFS/ topological
# sort of the graph.


opposite = {
    "N": "S",
    "S": "N",
    "E": "W",
    "W": "E",
    "NE": "SW",
    "NW": "SE",
    "SE": "NW",
    "SW": "NE",
}


def shared_direction(d1, d2):
    # check if they have any components in common
    return len(set(d1).intersection(set(d2))) != 0


def is_acyclic(graph):
    seen = set()
    def _DFS(node, path):
        path.add(node)
        seen.add(node)
        acyclic = True
        if node in graph:
            for next in graph[node]:
                if next in path:  # not a DAG
                    return False
                if next not in seen:
                    acyclic = acyclic and _DFS(next, path)
                if not acyclic:  # short-circuit
                    return False
            path.remove(node)
        return acyclic
    
    for node in graph:
        if node not in seen:
            if not _DFS(node, set()):
                return False
    return True
    

def check_direction(rules, dir):
    graph = DefaultDict(list)
    for f, d, t in rules:
        if shared_direction(d, dir):
            graph[f].append(t)
        if shared_direction(opposite[d], dir):
            graph[t].append(f)
    return is_acyclic(graph)


def check_validity(rules):
    # We need to make sure that all the horizontal and vertical
    # relationships are valid.
    return check_direction(rules, "N") and check_direction(rules, "E")


def test_direction():
    data = [
        ("A", "N",  "B"),
        ("B", "NE", "C"),
        ("C", "N",  "A")
    ]
    assert check_direction(data, "N") is False
    assert check_direction(data, "S") is False
    assert check_direction(data, "E") is True
    assert check_direction(data, "W") is True
    assert check_validity(data) is False


if __name__ == "__main__":
    test_direction()
    