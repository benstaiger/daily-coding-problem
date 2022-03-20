
# This problem was asked by Google.
# 
# Given a linked list, sort it in O(n log n) time and constant space.
# 
# For example, the linked list 4 -> 1 -> -3 -> 99 should become
# -3 -> 1 -> 4 -> 99.

class ListNode():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    @staticmethod
    def from_iterable(iter):
        first = None
        last = None
        for v in iter:
            if first is None:
                first = ListNode(v)
                last = first
            else:
                last.next = ListNode(v)
                last = last.next
        return first
    
    def __repr__(self):
        return f"{self.value} -> {self.next}"

    def __le__(self, other):
        return self.value < other.value
    
    def len(self):
        tmp = self
        length = 1
        while tmp.next:
            tmp = tmp.next
            length += 1
        return length


def sorted_merge(list1, list2):
    # iterate through two sorted lists and merge.
    if list1.value > list2.value:
        begin = list2
        list2 = list2.next
        begin.next = None
    else:
        begin = list1
        list1 = list1.next
        begin.next = None
    end = begin
    while list1 and list2:
        if list1.value > list2.value:
            end.next = list2
            list2 = list2.next
            end = end.next
            end.next = None
        else:
            end.next = list1
            list1 = list1.next
            end = end.next
            end.next = None
    
    if list1:
        end.next = list1
    if list2:  # mutually exclusive
        end.next = list2
    while end.next:
        end = end.next
    return begin, end


def break_chain(linked_list, length):
    if linked_list is None:
        return None, None
    begin = linked_list
    length -= 1
    while length > 0 and linked_list.next:
        linked_list = linked_list.next
        length -= 1
    rest = linked_list.next
    linked_list.next = None
    return begin, rest 


def sort_list(linked_list):
    # merge sort feels amenable to this
    group_size = 1
    length = linked_list.len()
    beginning = linked_list # everything before what we're working on
    while group_size < length:
        # make groups of group_size
        completed = None  # merged portion of list
        first_group, rest = break_chain(beginning, group_size)
        second_group, rest = break_chain(rest, group_size)
        beginning = None

        while first_group and second_group:
            new_chain, new_chain_end = sorted_merge(first_group, second_group)
            if beginning is None:
                beginning = new_chain
                completed = new_chain_end
            else:
                completed.next = new_chain
                completed = new_chain_end
            first_group, rest = break_chain(rest, group_size)
            second_group, rest = break_chain(rest, group_size)

        # Add any uneven chain segments to the end.
        if first_group and rest is None:
            completed.next = first_group
        elif second_group:
            raise "Something went wrong!!"
        group_size *= 2
    
    # final merge
    if length / (group_size / 2) > 2:
        raise "something went wrong with the merges!!"

    return beginning


def test_merge():
    sorted1 = ListNode.from_iterable([1, 3, 99])
    sorted2 = ListNode.from_iterable([2, 7, 91])
    expected = "1 -> 2 -> 3 -> 7 -> 91 -> 99 -> None" 
    begin, end = sorted_merge(sorted1, sorted2)
    assert str(begin) == expected
    assert end.value == 99 and end.next is None

    sorted1 = ListNode.from_iterable([1, 3, 99])
    sorted2 = ListNode.from_iterable([2, 7, 91])
    begin, end = sorted_merge(sorted2, sorted1)
    assert str(begin) == expected
    assert end.value == 99 and end.next is None


def test_break_chain():
    example = ListNode.from_iterable([4, 1, -3, 99])
    first, second = break_chain(example, 3)
    assert str(first) == "4 -> 1 -> -3 -> None"
    assert str(second) ==  "99 -> None"

    example = ListNode.from_iterable([4, 1, -3, 99])
    first, second = break_chain(example, 5)
    assert str(first) == "4 -> 1 -> -3 -> 99 -> None"
    assert second is None


def test_sort_list():
    # For example, the linked list 4 -> 1 -> -3 -> 99 should become
    # -3 -> 1 -> 4 -> 99.
    example = ListNode.from_iterable([4, 1, -3, 99])
    result = sort_list(example)
    assert str(result) == "-3 -> 1 -> 4 -> 99 -> None"

    example = ListNode.from_iterable([6, 7, 88, 9, 4, 3, 1, -3, 99])
    expected = "-3 -> 1 -> 3 -> 4 -> 6 -> 7 -> 9 -> 88 -> 99 -> None"
    result = sort_list(example)
    assert str(result) == expected


if __name__ == "__main__":
    test_merge()
    test_break_chain()
    test_sort_list()
