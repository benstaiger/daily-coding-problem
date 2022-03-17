import heapq
from collections import defaultdict

# This problem was asked by Amazon.
# 
# Huffman coding is a method of encoding characters based on their frequency.
# Each letter is assigned a variable-length binary string, such as 0101 or
# 111110, where shorter lengths correspond to more common letters. To
# accomplish this, a binary tree is built such that the path from the root to
# any leaf uniquely maps to a character. When traversing the path, descending
# to a left child corresponds to a 0 in the prefix, while descending right
# corresponds to 1.
# 
# Here is an example tree (note that only the leaf nodes have letters):
# 
#         *
#       /   \
#     *       *
#    / \     / \
#   *   a   t   *
#  /             \
# c               s
# With this encoding, cats would be represented as 0000110111.
# 
# Given a dictionary of character frequencies, build a Huffman tree, and use it
# to determine a mapping between characters and their encoded binary strings.


class Tree():
    def __init__(self, letter=None, left=None, right=None):
        self.left = left
        self.right = right
        self.letter = letter

    def __repr__(self):
        left_str = ""
        right_str = ""
        if self.left:
            left_str = self.left.__repr__()
        if self.right:
            right_str = self.right.__repr__()
        if self.letter:
            return self.letter
        return f"({left_str}, {right_str})"
    
    def __lt__(self, other):
        return False # all trees are greater than all other trees...


def huffman_tree(freq_dict) -> Tree:
    # The important thing about huffman encoding that was left out of the
    # is its relationship to optimal encoding length. A true huffman coding
    # will minimize the length of the text.
    min_heap = []
    for k, v in freq_dict.items():
        heapq.heappush(min_heap, (v, Tree(k)))

    # Nodes with the lowest scores will end up being the deepest in the tree.
    while len(min_heap) > 1:
        score1, smallest1 = heapq.heappop(min_heap)
        score2, smallest2 = heapq.heappop(min_heap)
        new_node = Tree(None, smallest1, smallest2)
        heapq.heappush(min_heap, (score1+score2, new_node))

    score, tree = heapq.heappop(min_heap)
    return tree


def test_huffman_tree():
    test_str = "this is a test of the encoding pattern"
    freq = defaultdict(int)
    for v in test_str:
        freq[v] += 1
    
    huff_tree = huffman_tree(freq)
    print(f"sentence: {test_str}")
    print(f"freq: {freq}")
    print(huff_tree)

    depths = {}
    def dfs(tree, depth=0):
        if tree.letter:
            depths[tree.letter] = depth
        if tree.right:
            dfs(tree.right, depth+1)
        if tree.left:
            dfs(tree.left, depth+1)
    
    dfs(huff_tree)
    print(f"depths: {depths}")


if __name__ == "__main__":
    test_huffman_tree()
