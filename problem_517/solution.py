
# This problem was asked by Google.
# 
# Given two singly linked lists that intersect at some point, find the
# intersecting node. The lists are non-cyclical.
# 
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return
# the node with value 8.
# 
# In this example, assume nodes with the same value are the exact same node
# objects.
# 
# Do this in O(M + N) time (where M and N are the lengths of the lists) and
# constant space.


class ListNode():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def rev_list(linked_list):
    tmp = linked_list
    while linked_list.next:
        next = linked_list.next
        tmp = ListNode(next.value, tmp)
        linked_list = linked_list.next
    return tmp
    

def intersection_point(list1, list2):
    # reverse both linked lists and find the point where they deviate
    # It really depends on the definition of intersect is.
    # We could also check the value of the memory addresses instead to see
    # if they are the same object rather than the same pattern using id().
    rev1 = rev_list(list1)
    rev2 = rev_list(list2)
    last_seen = None
    while rev1.value == rev2.value:
        last_seen = rev1.value
        rev1 = rev1.next
        rev2 = rev2.next
    return last_seen


def test_intersection():
    # A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10
    a = ListNode(3, ListNode(7, ListNode(8, ListNode(10))))
    b = ListNode(99, ListNode(1, ListNode(8, ListNode(10))))

    print(intersection_point(a, b))


if __name__ == "__main__":
    test_intersection()
