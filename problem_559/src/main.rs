use std::cmp::Reverse;
use std::collections::{BinaryHeap, LinkedList};

// This problem was asked by Google.
//
// Given k sorted singly linked lists, write a function to merge all the lists
// into one sorted singly linked list.

fn merge_lists<T: Ord>(mut lists: Vec<LinkedList<T>>) -> LinkedList<T> {
    let mut result = LinkedList::new();
    let mut smallest = BinaryHeap::new();

    // create a heap with the (value, idx) pairs for the first value
    // at the front of every list.
    for (i, list) in lists.iter_mut().enumerate() {
        if let Some(v) = list.pop_front() {
            smallest.push((Reverse(v), i));
        }
    }

    while !smallest.is_empty() {
        // insert the next smallest item into the result list
        let (Reverse(v), i) = smallest.pop().unwrap();
        result.push_back(v);

        // push the next value from the previously popped list into the heap.
        if let Some(v) = lists[i].pop_front() {
            smallest.push((Reverse(v), i));
        }
    }

    result
}

fn main() {
    let list1: LinkedList<i32> = vec![1, 3, 4, 5, 5].into_iter().collect();
    let list2: LinkedList<i32> = vec![1, 2, 2, 2, 5].into_iter().collect();
    let list3: LinkedList<i32> = vec![4, 5, 7, 8, 9].into_iter().collect();

    let lists = vec![list1, list2, list3];
    let merged_lists = merge_lists(lists);
    let expected: LinkedList<i32> = vec![1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 7, 8, 9]
        .into_iter()
        .collect();
    assert_eq!(merged_lists, expected);
}
