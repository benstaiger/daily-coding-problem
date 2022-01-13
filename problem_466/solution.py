
# This problem was asked by Amazon.
# 
# A tree is symmetric if its data and shape remain unchanged when it is
# reflected about the root node. The following tree is an example:
# 
#         4
#       / | \
#     3   5   3
#   /           \
# 9              9
#
# Given a k-ary tree, determine whether it is symmetric.


class Tree:
    def __init__(self, value):
        self._value = value
        self._children = []
        self._parent = None
    
    def add(self, tree):
        self._children.append(tree)
        tree._parent = self
    
    def children(self):
        return self._children
    
    @property
    def value(self):
        return self._value


def fwd_traversal(tree):
    yield tree 
    for t in tree.children():
        yield from fwd_traversal(t)


def rev_traversal(tree):
    yield tree
    for t in reversed(tree.children()):
        yield from rev_traversal(t)


def check_symmetry(tree):
    for a, b in zip(fwd_traversal(tree), rev_traversal(tree)):
        print(a.value, b.value)
        if a.value != b.value or len(a.children()) != len(b.children()):
            return False
    return True


def test_check_symmetry():
    # test symmetric:
    #         4
    #       / | \
    #     3   5   3
    #   /           \
    # 9              9
    root = Tree(4)
    t1 = Tree(3)
    t1.add(Tree(9))
    t2 = Tree(5)
    t3 = Tree(3)
    t3.add(Tree(9))
    root.add(t1)
    root.add(t2)
    root.add(t3)
    assert check_symmetry(root)
    root.add(Tree(6))
    assert check_symmetry(root) is False


if __name__ == "__main__":
    test_check_symmetry()
