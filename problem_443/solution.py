# This problem was asked by Apple.

# Implement a queue using two stacks. Recall that a queue is a FIFO
# (first-in, first-out) data structure with the following methods: enqueue,
# which inserts an element into the queue, and dequeue, which removes it.

class SQueue:
    def __init__(self):
        self._stack1 = []
        self._stack2 = []
    
    def top(self):
        if self._stack1:
            return self._stack1[-1]
        else:
            return None

    def push(self, value):
        while self._stack1:
            self._stack2.append(self._stack1.pop())
        
        self._stack1.append(value)
        while self._stack2:
            self._stack1.append(self._stack2.pop())

    def pop(self):
        if self._stack1:
            return self._stack1.pop()
        else:
            return None


def test_queue():
    queue = SQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    assert queue.top() == 1
    queue.pop()
    assert queue.top() == 2
    queue.pop()
    assert queue.top() == 3
    queue.pop()
    assert queue.top() is None


if __name__ == "__main__":
    test_queue()
