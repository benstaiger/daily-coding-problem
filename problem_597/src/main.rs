use std::collections::HashMap;

// This problem was asked by Netflix.
//
// Given an array of integers, determine whether it contains a Pythagorean
// triplet. Recall that a Pythogorean triplet (a, b, c) is defined by the
// equation a2 + b2 = c2.

fn find_pythag_triple(data: &[i32]) -> Option<(i32, i32, i32)> {
    let seen: HashMap<i32, usize> =
        HashMap::from_iter(data.iter().enumerate().map(|(i, &x)| (x, i)));

    for (i, v1) in data.iter().enumerate() {
        for (j, v2) in data.iter().enumerate() {
            let target = ((v1 * v1 + v2 * v2) as f32).sqrt() as i32;
            if let Some(&k) = seen.get(&target) {
                if k != i && k != j && i != j {
                    return Some((*v1, *v2, target));
                }
            }
        }
    }
    None
}

fn main() {
    println!(
        "tuple {:?}",
        find_pythag_triple(&vec![1, 2, 3, 4, 54, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    );
}
