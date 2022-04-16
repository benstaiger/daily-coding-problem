use std::borrow::Cow;

// This problem was asked by Facebook.
//
// Given an array of integers, write a function to determine whether the array
// could become non-decreasing by modifying at most 1 element.
//
// For example, given the array [10, 5, 7], you should return true, since we
// can modify the 10 into a 1 to make the array non-decreasing.
//
// Given the array [10, 5, 1], you should return false, since we can't modify
// any one element to get a non-decreasing array.

fn almost_nondecreasing(data: &[i32]) -> bool {
    if data.len() < 2 {
        return true;
    }

    // The check could be done in a completely const manner by checking the values
    // surrounding the nondecreasing point, but this was a bit more concise.
    let mut data = Cow::from(data);
    let mut num_nondecreasing = 0;
    for i in 1..data.len() {
        if data[i] < data[i-1] {
            // Make a valid substitution for the value.
            if i == 1 {
                // boundary condition
                data.to_mut()[i-1] = data[i];
            } else {
                data.to_mut()[i] = data[i-1];
            }
            num_nondecreasing += 1;
        }
        if num_nondecreasing > 1 {
            return false;
        }
    }
    return true;
}

fn main() {
    assert!(almost_nondecreasing(&vec![10, 100, 12]));  // middle value
    assert!(almost_nondecreasing(&vec![10, 15, 7]));  // last value
    assert!(almost_nondecreasing(&vec![10, 5, 7]));  // first value
    assert!(!almost_nondecreasing(&vec![10, 5, 1]));  // no options
}
