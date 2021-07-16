import heapq

# This problem was asked by Quora.
#
# You are given a list of (website, user) pairs that represent users visiting
# websites. Come up with a program that identifies the top k pairs of websites
# with the greatest similarity.
#
# For example, suppose k = 1, and the list of tuples is:
#
# [('a', 1), ('a', 3), ('a', 5),
#  ('b', 2), ('b', 6),
#  ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5)
#  ('d', 4), ('d', 5), ('d', 6), ('d', 7),
#  ('e', 1), ('e', 3), ('e': 5), ('e', 6)]
# Then a reasonable similarity metric would most likely conclude that a and e
# are the most similar, so your program should return [('a', 'e')].


def create_adjacency_matrix(user_list):
    user_websites = {}
    for w, u in user_list:
        if u not in user_websites:
            user_websites[u] = []
        user_websites[u].append(w)

    similarity_matrix = {}
    for u, webs in user_websites.items():
        # for every pair of websites, add a pair.
        webs = sorted(webs)
        for i in range(len(webs) - 1):
            for j in range(i + 1, len(webs)):
                web_pair = (webs[i], webs[j])
                if web_pair not in similarity_matrix:
                    similarity_matrix[web_pair] = 0
                similarity_matrix[web_pair] += 1
    return similarity_matrix


def find_top_k(iterable_key_val, K):
    # We want to iterate and maintain a heap of size K while we iterate to
    # find the top K.
    #
    # Essentially, we will keep a min-queue of the top K and if the value
    # we see if greater than the smallest of our current top K, we will
    # replace the smallest value.
    top_k = []
    for k, v in iterable_key_val.items():
        if len(top_k) < K:
            heapq.heappush(top_k, (v, k))
        elif v > top_k[0][0]:
            heapq.heapreplace(top_k, (v, k))
    top_k = sorted(top_k, key=lambda x: x[0])
    return [k for _, k in top_k]


def test_find_top_k():
    assert find_top_k({i: i for i in range(10)}, 3) == list(range(10-3, 10))
    letters = "kjdalsivms"
    assert find_top_k({letters[i]: i for i in range(10)}, 3) == [
        letters[j] for j in range(10-3, 10)
    ]


def find_top_websites(user_list, K):
    similarity_matrix = create_adjacency_matrix(user_list)
    return find_top_k(similarity_matrix, K)


def test_find_top_websites():
    user_list = [
        ("a", 1),
        ("a", 3),
        ("a", 5),
        ("b", 2),
        ("b", 6),
        ("c", 1),
        ("c", 2),
        ("c", 3),
        ("c", 4),
        ("c", 5),
        ("d", 4),
        ("d", 5),
        ("d", 6),
        ("d", 7),
        ("e", 1),
        ("e", 3),
        ("e", 5),
        ("e", 6),
    ]
    print(find_top_websites(user_list, 1))


if __name__ == "__main__":
    test_find_top_k()
    test_find_top_websites()
