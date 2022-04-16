// This problem was asked by Amazon.
//
// An sorted array of integers was rotated an unknown number of times.
//
// Given such an array, find the index of the element in the array in faster
// than linear time. If the element doesn't exist in the array, return null.
//
// For example, given the array [13, 18, 25, 2, 8, 10] and the element 8,
// return 4 (the index of 8 in the array).
//
// You can assume all the integers in the array are unique.

/// Find the rotation point of an otherwise sorted array by modified binary search
fn find_rotation(rotated: &[i32]) -> usize {
    // we know that if it was rotated K positions, then all values at index < K must be
    // <= the first value, and all positions >= K will be less than the first value.
    let mut left = 0;
    let mut right = rotated.len() - 1;
    
    while left < right {
        let mid = (right + left) / 2;
        if rotated[mid] > rotated[0] {
            left = mid + 1;
        } else if rotated[mid] < rotated[0] {
            right = mid;
        }
    }

    // in the event that we aren't rotated, we would just return the right-most element
    if rotated[right] > rotated[0]{
        0
    } else {
        right
    }
}

/// If the values exists in a rotated array, return its index. Otherwise
/// return None.
fn rotated_binary_search(rotated: &[i32], value: i32) -> Option<usize> {
    let start = find_rotation(rotated);

    // binary search the sub arrays.
    if let Ok(idx) = rotated[0..start].binary_search(&value) {
        return Some(idx);
    }
    if let Ok(idx) = rotated[start..rotated.len()].binary_search(&value) {
        return Some(start + idx);
    }
    return None;


}

fn main() {
    assert_eq!(
        find_rotation(&vec![13, 18, 25, 2, 8, 10]),
        3
    );
    assert_eq!(
        rotated_binary_search(&vec![13, 18, 25, 2, 8, 10], 8),
        Some(4)
    );
}
