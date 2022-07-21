

# This problem was asked by Twitter.
# 
# A classroom consists of N students, whose friendships can be represented in
# an adjacency list. For example, the following descibes a situation where 0 is
# friends with 1 and 2, 3 is friends with 6, and so on.
# 
# {0: [1, 2],
#  1: [0, 5],
#  2: [0],
#  3: [6],
#  4: [],
#  5: [1],
#  6: [3]} 
# Each student can be placed in a friend group, which can be defined as the
# transitive closure of that student's friendship relations. In other words,
# this is the smallest set such that no student in the group has any friends
# outside this group. For the example above, the friend groups would be
# {0, 1, 2, 5}, {3, 6}, {4}.
# 
# Given a friendship list such as the one above, determine the number of friend
# groups in the class.


def transitive_closure(adjacency):
    # I will assume that all relationships are symmetric.
    # They don't HAVE to be, but it means that I know that if I find anyone
    # within a given group. I am guaranteed to find ALL people within the group
    # because there is no option for a node to be a "source" node. Otherwise,
    # we will simply have to "merge" groups if we run into another group while
    # searching.

    # We will simply perform a DFS to identify a groups. If anyone is not
    # included in the first DFS, we will start another one at the unseen person
    # identifying the next group.

    seen = {}

    def dfs(node, group):
        seen[node] = group
        for a in adjacency[node]:
            if a not in seen:
                dfs(a, group)
    
    group_num = 0
    for a in adjacency:
        if a not in seen:
            dfs(a, group_num)
            group_num += 1
    
    return group_num


def test_transitive_closure():
    example = {
        0: [1, 2],
        1: [0, 5],
        2: [0],
        3: [6],
        4: [],
        5: [1],
        6: [3],
    } 
    assert transitive_closure(example) == 3


if __name__ == "__main__":
    test_transitive_closure()
