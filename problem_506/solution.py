
# This problem was asked by Fitbit.
# 
# Given a linked list, rearrange the node values such that they appear in
# alternating low -> high -> low -> high ... form. For example, given
# 1 -> 2 -> 3 -> 4 -> 5, you should return 1 -> 3 -> 2 -> 5 -> 4.


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    @staticmethod
    def from_iterable(it):
        first = None
        last = None
        for v in it:
            if first is None:
                first = ListNode(v)
                last = first
            else:
                last.next = ListNode(v)
                last = last.next
        return first
    
    def __repr__(self):
        return f"{self.value} -> {self.next}"


def swap_this_next(prev, this, next):
    this.next = next.next
    next.next = this
    prev.next = next


def alternating(linked_list):
    # ensure it starts with a low value
    if linked_list.value > linked_list.next.value:
        tmp = linked_list.next
        linked_list.next = tmp.next
        tmp.next = linked_list
        linked_list = tmp

    low = False
    prev = linked_list
    this = linked_list.next
    while this.next:
        if low and this.next.value < this.value:
            swap_this_next(prev, this, this.next)
        elif not low and this.next.value > this.value:
            swap_this_next(prev, this, this.next)
        else:
            this = this.next
        low = low ^ True
        prev = prev.next
    return linked_list


def test_alternating():
    example = ListNode.from_iterable([1, 2, 3, 4, 5]) 
    print(alternating(example))

    example = ListNode.from_iterable([2, 1, 3, 4, 5]) 
    print(alternating(example))


if __name__ == "__main__":
    test_alternating()
