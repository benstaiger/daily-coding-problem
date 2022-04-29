// This problem was asked by Google.
//
// You are given an N by M 2D matrix of lowercase letters. Determine the
// minimum number of columns that can be removed to ensure that each row is
// ordered from top to bottom lexicographically. That is, the letter at each
// column is lexicographically later as you go down each row. It does not
// matter whether each row itself is ordered lexicographically.
//
// For example, given the following table:
//
// cba
// daf
// ghi
// This is not ordered because of the a in the center. We can remove the second
// column to make it ordered:
//
// ca
// df
// gi
// So your function should return 1, since we only needed to remove 1 column.
//
// As another example, given the following table:
//
// abcdef
// Your function should return 0, since the rows are already ordered (there's
// only one row).
//
// As another example, given the following table:
//
// zyx
// wvu
// tsr
// Your function should return 3, since we would need to remove all the columns
// to order it.

use std::str::Utf8Error;

fn find_reduced_sorted(strs: &[&str]) -> usize {
    let mut removed = vec![false; strs[0].len()];
    let mut to_remove = 0;

    for i in 1..strs.len() {
        let prev_row = strs[i - 1].as_bytes();
        let cur_row = strs[i].as_bytes();
        for j in 0..prev_row.len() {
            if !removed[j] && prev_row[j] > cur_row[j] {
                removed[j] = true;
                to_remove += 1;
            }
        }
    }
    to_remove
}

fn chunk_str(data: &str, chunk_size: usize) -> Result<Vec<&str>, Utf8Error> {
    data.as_bytes()
        .chunks(chunk_size)
        .map(std::str::from_utf8)
        .collect::<Result<Vec<&str>, _>>()
}

fn main() {
    let data = chunk_str("cbadafghi", 3).unwrap();
    assert_eq!(find_reduced_sorted(&data), 1);
    let data = chunk_str("cadfgi", 2).unwrap();
    assert_eq!(find_reduced_sorted(&data), 0);
    let data = chunk_str("abcdef", 6).unwrap();
    assert_eq!(find_reduced_sorted(&data), 0);
    let data = chunk_str("zyxwvutsr", 3).unwrap();
    assert_eq!(find_reduced_sorted(&data), 3);
}
