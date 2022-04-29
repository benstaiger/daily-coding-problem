
// This problem was asked by Etsy.
//
// Given a sorted array, convert it into a height-balanced binary search tree.

#[derive(Debug)]
struct Tree {
    value: i32,
    left: Option<Box<Tree>>,
    right: Option<Box<Tree>>,
}

fn height_balance(sorted: &[i32]) -> Option<Box<Tree>> {
    fn height_balance_help(sorted: &[i32], left: usize, right: usize) -> Option<Box<Tree>> {
        if left > right {
            return None;
        }

        let middle = (left + right) / 2;
        Some(Box::new(Tree {
            value: sorted[middle],
            left: if middle > 0 {
                height_balance_help(sorted, left, middle - 1)
            } else {
                None
            },
            right: height_balance_help(sorted, middle + 1, right),
        }))
    }

    height_balance_help(sorted, 0, sorted.len() - 1)
}

fn main() {
    let result = height_balance(&vec![0, 1, 2, 3, 4, 5, 6]).unwrap();
    println!("{:?}", &result);
    assert_eq!(result.value, 3);
    assert_eq!(result.left.unwrap().value, 1);
    assert_eq!(result.right.unwrap().value, 5);
}
