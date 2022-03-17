
# This problem was asked by LinkedIn.
# 
# Given a linked list of numbers and a pivot k, partition the linked list so
# that all nodes less than k come before nodes greater than or equal to k.
# 
# For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, the
# solution could be 1 -> 0 -> 5 -> 8 -> 3.


class ListNode():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def __repr__(self):
        return f"{self.value} -> {self.next}"


def partition_inplace(linked_list, pivot):
    less_list_begin = ListNode(None, None)
    less_list_end = less_list_begin
    more_list_begin = ListNode(None, None)
    more_list_end = more_list_begin

    while linked_list:
        if linked_list.value < pivot:
            less_list_end.next = linked_list
            less_list_end = less_list_end.next
            linked_list = linked_list.next
            less_list_end.next = None
        else:
            more_list_end.next = linked_list
            more_list_end = more_list_end.next
            linked_list = linked_list.next
            more_list_end.next = None
    
    if more_list_begin.next:
        more_list = more_list_begin.next
        if less_list_begin.next:
            less_list_end.next = more_list
            less_list = less_list_begin.next
            return less_list
        else:
            return more_list
    elif less_list_begin.next:
            less_list = less_list_begin.next
            return less_list
    else:
        return None


def test_partition_inplace():
    # For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, the
    # solution could be 1 -> 0 -> 5 -> 8 -> 3.
    example = ListNode(5, ListNode(1, ListNode(8, ListNode(0, ListNode(3)))))
    fixed = partition_inplace(example, 3)
    assert str(fixed) == "1 -> 0 -> 5 -> 8 -> 3 -> None"

if __name__ == "__main__":
    test_partition_inplace()
