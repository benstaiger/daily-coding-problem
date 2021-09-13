
# This problem was asked by Zillow.
# 
# A ternary search tree is a trie-like data structure where each node may have
# up to three children. Here is an example which represents the words code,
# cob, be, ax, war, and we.
# 
#        c
#     /  |  \
#    b   o   w
#  / |   |   |
# a  e   d   a
# |    / |   | \ 
# x   b  e   r  e  
# The tree is structured according to the following rules:
# 
# * left child nodes link to words lexicographically earlier than the parent
# prefix
# * right child nodes link to words lexicographically later than the parent
# prefix
# * middle child nodes continue the current word
#
# For instance, since code is the first word inserted in the tree, and cob
# lexicographically precedes cod, cob is represented as a left child extending
# from cod.
# 
# Implement insertion and search functions for a ternary search tree.

class TernaryTree:
    def __init__(self):
        self.letter = None
        self.left = None
        self.right = None
        self.middle = None

    def prefix_find(self, word):
        """
        Find the node within the tree with the longest prefix of the input.
        Returns the node and the remaining suffix.
        """
        if not self.letter:
            return self, word

        suffix = word[1:]
        if word[0] < self.letter:
            if not self.left:
                return self, word
            return self.left.prefix_find(word)
        if word[0] == self.letter:
            if not self.middle:
                return self, suffix
            return self.middle.prefix_find(suffix)
        if word[0] > self.letter:
            if not self.right:
                return self, word
            return self.right.prefix_find(word)

    def insert(self, word):
        tree, remaining = self.prefix_find(word)

        suffix = remaining[1:]
        if tree.letter is None:
            tree.letter = remaining[0]
        elif remaining[0] < tree.letter:
            tree.left = TernaryTree()
            tree.left.letter = remaining[0]
            tree = tree.left
        elif remaining[0] == tree.letter:
            tree.middle = TernaryTree()
            tree.middle.letter = remaining[0]
            tree = tree.middle
        elif remaining[0] > tree.letter:
            tree.right = TernaryTree()
            tree.right.letter = remaining[0]
            tree = tree.right

        for w in suffix:
            tree.middle = TernaryTree()
            tree.middle.letter = w
            tree = tree.middle

    def search(self, word):
        tree, suffix = self.prefix_find(word)
        return suffix == ""

    def __repr__(self):
        def cond_create(tree):
            return "" if not tree else tree.__repr__()
        kids = [cond_create(t) for t in [self.left, self.middle, self.right]]
        return f"{self.letter}: [{', '.join(kids)}]" 


def test_prefix_find():
    def construct(letter):
        ret = TernaryTree()
        ret.letter = letter
        return ret

    root = construct("c")
    root.middle = construct("o")
    root.right = construct("w")
    root.right.middle = construct("a")
    root.right.middle.middle = construct("r")
    tree, suffix = root.prefix_find("we")
    assert tree.letter == "a"
    assert suffix == "e"


def test_insert():
    root = TernaryTree()
    root.insert("code")
    root.insert("cob")
    root.insert("be")
    root.insert("ax")
    root.insert("war")
    root.insert("we")
    assert root.letter == "c"
    assert root.left.letter == "b"
    assert root.middle.letter == "o"
    assert root.right.letter == "w"
    assert root.middle.middle.left.letter == "b"


def test_search():
    root = TernaryTree()
    root.insert("code")
    root.insert("cob")
    root.insert("be")
    root.insert("ax")
    root.insert("war")
    root.insert("we")
    assert root.search("cob")
    assert root.search("we")
    assert root.search("cobbler") is False


if __name__ == "__main__":
    test_prefix_find()
    test_insert()
    test_search()

