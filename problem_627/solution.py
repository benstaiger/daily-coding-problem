

# This problem was asked by Google.
# 
# Given an iterator with methods next() and hasNext(), create a wrapper
# iterator, PeekableInterface, which also implements peek(). peek shows the
# next element that would be returned on next().
# 
# Here is the interface:

class PeekableInterface(object):
    def __init__(self, iterator):
        self.it = iterator
        self.has_next = True
        try:
            self.next_item = next(iterator)
        except:
            self.has_next = False
            self.next_item = None

    def peek(self):
        return self.next_item

    def next(self):
        tmp = self.next_item
        try:
            self.next_item = next(self.it)
        except:
            self.has_next = False
            self.next_item = None
        return tmp

    def hasNext(self):
        return self.has_next


def test_peekable():
    peekable = PeekableInterface(iter(range(10)))
    i = 0
    while peekable.hasNext():
        assert peekable.next() == i
        i += 1

    peekable = PeekableInterface(iter(range(10)))
    for i in range(5):
        assert peekable.next() == i
    for i in range(5):
        assert peekable.peek() == 5
    for i in range(5, 10):
        assert peekable.next() == i
    


if __name__ == "__main__":
    test_peekable()
