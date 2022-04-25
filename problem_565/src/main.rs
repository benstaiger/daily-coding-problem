use std::cmp::max;

// This problem was asked by Pinterest.
// 
// Given an integer list where each number represents the number of hops you
// can make, determine whether you can reach to the last index starting at index 0.
// 
// For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.

fn can_hop_to_end(hops: &[usize]) -> bool {
    // For each space, we will keep track of whether or not it is reachable as
    // well as the furthest reachable space. 
    let mut furthest_reachable = 0;
    for (i, v) in hops.iter().enumerate() {
        if i > furthest_reachable {
            break
        }
        furthest_reachable = max(furthest_reachable, i + v);
    }
    furthest_reachable >= hops.len() - 1
}

fn main() {
    assert!(can_hop_to_end(&vec![2, 0, 1, 0]));
    assert!(!can_hop_to_end(&vec![1, 1, 0, 1]));
}
