

# This problem was asked by Google.
# 
# Given a singly linked list and an integer k, remove the kth last element from
# the list. k is guaranteed to be smaller than the length of the list.
# 
# The list is very long, so making more than one pass is prohibitively
# expensive.
# 
# Do this in constant space and in one pass.

class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def __repr__(self):
        return f"{self.value}{self.next}"


def remove_elements(linked_list, k):
    if k == 0:
        tmp = linked_list.next
        linked_list.next = None 
        return tmp

    prev = None
    curr = linked_list
    i = 0
    while i < k:
        if not prev:
            prev = curr
        else:
            prev = prev.next 
            curr = curr.next
        k += 1

    prev.next = curr.next
    curr.next = None
    return linked_list
