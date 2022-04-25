
// This problem was asked by Google.
//
// Given a sorted list of integers, square the elements and give the output in sorted order.
//
// For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].

fn squared_merge(sorted: &[i32]) -> Vec<i32> {
    let mut result: Vec<i32> = vec![0; sorted.len()];
    if result.len() == 0 {
        return result;
    }
    let mut insert_idx = result.len() - 1;
    let mut fwd_idx = 0;
    let mut rev_idx = sorted.len() - 1;

    while fwd_idx <= rev_idx {
        let fwd_sqr = sorted[fwd_idx] * sorted[fwd_idx];
        let rev_sqr = sorted[rev_idx] * sorted[rev_idx];
        if fwd_sqr > rev_sqr {
            result[insert_idx] = fwd_sqr;
            fwd_idx += 1;
        } else {
            result[insert_idx] = rev_sqr;
            rev_idx -= 1;
        }
        if insert_idx > 0 {
            insert_idx -= 1;
        }
    }
    result
}

fn main() {
    println!("{:?}", squared_merge(&vec![-9, -2, 0, 2, 3]));
}
