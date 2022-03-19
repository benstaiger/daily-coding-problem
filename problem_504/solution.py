
# This problem was asked by Twitter.
# 
# You run an e-commerce website and want to record the last N order ids in a
# log. Implement a data structure to accomplish this, with the following API:
# 
# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be
# smaller than or equal to N.
# You should be as efficient with time and space as possible.


class CircularBuffer():
    def __init__(self, N):
        self.buffer = [None for _ in range(N)]
        self.next_index = 0

    def insert_next(self, val):
        self.buffer[self.next_index] = val
        self.next_index += 1
        self.next_index = self.next_index % len(self.buffer)
    
    def get_prev(self, idx_ago):
        idx = (self.next_index - 1 - idx_ago) % len(self.buffer)
        return self.buffer[idx]


# do we actually need to keep all order_ids :p
class OrderLog():
    def __init__(self, N):
        self.circ_buffer = CircularBuffer(N)
    
    def record(self, order_id):
        self.circ_buffer.insert_next(order_id)
    
    def get_last(self, idx):
        return self.circ_buffer.get_prev(idx)