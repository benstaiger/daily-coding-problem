use std::cmp::max;

// This problem was asked by Airbnb.
// 
// Given a list of integers, write a function that returns the largest sum of
// non-adjacent numbers. Numbers can be 0 or negative.
// 
// For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
// [5, 1, 1, 5] should return 10, since we pick 5 and 5.
// 
// Follow-up: Can you do this in O(N) time and constant space?

fn best_sum(values: &[i32]) -> i32 {
    // find the best sum up to every position
    // the "best sum" at a given position is either including the value + the
    // best sum up to i-2 or the best sum at i-1.
    assert!(values.len() > 0);

    let mut prev_best = 0;  // best up to i-1
    let mut prev_prev_best = 0;  // best up to i-2
    for i in 0..values.len() {
        let best = max(prev_best, prev_prev_best + values[i]);
        prev_prev_best = prev_best;
        prev_best = best;
    }
    prev_best
}

fn main() {
    let example = vec![2, 4, 6, 2, 5];
    let best = best_sum(&example);
    assert_eq!(best, 13);

    let example = vec![5, 1, 1, 5];
    let best = best_sum(&example);
    assert_eq!(best, 10);
}
