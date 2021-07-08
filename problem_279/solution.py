# This problem was asked by Twitter.
#
# A classroom consists of N students, whose friendships can be represented in
# an adjacency list. For example, the following descibes a situation where 0
# is friends with 1 and 2, 3 is friends with 6, and so on.
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
# Given a friendship list such as the one above, determine the number of
# friend groups in the class.


def find_friend_groups(friends_list):
    """
    A clique, or transitive closure, can be found simply by performing a DFS
    to see which other students are reachable. Then continuing the process
    for each student until all students have been added to groups.

    This takes O(E + V) time.
    """

    groups = []
    in_group = [False for i in friends_list]
    active_group = set()

    def dfs(person):
        active_group.add(person)
        in_group[person] = True
        for other in friends_list[person]:
            if not in_group[other]:
                dfs(other)

    for person, friends in friends_list.items():
        if not in_group[person]:
            dfs(person)
            groups.append(active_group)
            active_group = set()

    return groups


if __name__ == "__main__":
    friends_list = {
        0: [1, 2],
        1: [0, 5],
        2: [0],
        3: [6],
        4: [],
        5: [1],
        6: [3],
    }
    print(find_friend_groups(friends_list))
