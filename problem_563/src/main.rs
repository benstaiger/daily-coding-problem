
// This problem was asked by Nvidia.
// 
// Find the maximum of two numbers without using any if-else statements, branching, or direct comparisons.

fn max(a: i32, b: i32) -> i32 {
    let flag: i32 = ((a - b) >> 31) & 1; // if a > b, then a-b is positive and the msb is 0 else 1.
    a * (1 - flag) + b * flag
}

fn main() {
    assert_eq!(2, max(2, 1));
    assert_eq!(2, max(1, 2));
}
