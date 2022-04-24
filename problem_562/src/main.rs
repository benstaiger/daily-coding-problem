// This problem was asked by Uber.
//
// Given an array of integers, return a new array such that each element at
// index i of the new array is the product of all the numbers in the original
// array except the one at i.
//
// For example, if our input was [1, 2, 3, 4, 5], the expected output would be
// [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
// be [2, 3, 6].
//
// Follow-up: what if you can't use division?

fn prod_div(data: &[i32]) -> Vec<i32> {
    let total: i32 = data.into_iter().product();
    data.iter().map(|&v| total / v).collect()
}

fn prod_no_div(data: &[i32]) -> Vec<i32> {
    let mut back_prod: Vec<i32> = data
        .iter()
        .rev()
        .scan(1, |acc, &v| {
            *acc = *acc * v;
            Some(*acc)
        })
        .collect();
    back_prod.reverse();
    let fwd_prod: Vec<i32> = data
        .iter()
        .scan(1, |acc, &v| {
            *acc = *acc * v;
            Some(*acc)
        })
        .collect();

    (0..data.len()).map(
        |i| if i > 0 { fwd_prod[i-1] } else { 1 } * if i < data.len() - 1 { back_prod[i+1] } else { 1 }
    ).collect()
}

fn main() {
    let example: Vec<i32> = (1..=5).collect();
    let expected = vec![120, 60, 40, 30, 24];

    assert_eq!(expected, prod_no_div(&example));
}
