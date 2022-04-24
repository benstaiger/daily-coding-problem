use std::collections::HashSet;

// This problem was recently asked by Google.
//
// Given a list of numbers and a number k, return whether any two numbers from
// the list add up to k.
//
// For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
//
// Bonus: Can you do this in one pass?

fn two_sum(vals: &[i32], target: i32) -> bool {
    let mut looking_for: HashSet<i32> = HashSet::new();
    for v in vals.iter() {
        if looking_for.contains(&v) {
            return true;
        }
        // Do this second. Otherwise a single instance of "target/2" would ret.
        looking_for.insert(target - v);
    }
    return false;
}

fn main() {
    let vals = vec![10, 15, 3, 7];
    assert!(two_sum(&vals, 17));
    assert!(!two_sum(&vals, 26));
}
