// This problem was asked by Google.
//
// You are given an array of length n + 1 whose elements belong to the set
// {1, 2, ..., n}. By the pigeonhole principle, there must be a duplicate. Find
// it in linear time and space.

fn pigeonhole(arr: &[u32]) -> u32 {
    // We know that there is a single value that will appear twice
    // sum(1 to N) = N * (N + 1) / 2
    // so we will find the actual total to infer the repeated value
    let n: u32 = arr.len().try_into().expect("Array too large.");
    // total of N elements, not N + 1
    // this is the actual statement that might overflow.
    let expected_total: u32 = n * (n - 1) / 2;
    let mut total = 0;
    for v in arr {
        total += v;
    }
    total - expected_total // ordering matters or we'll underflow.
}

fn pigeonhole2(arr: &[u32]) -> u32 {
    // a xor a = 0
    // a xor b xor a = b
    // if we xor our array and all values 1 to N then only the bits
    // of the value that appears 3 times will remain since all other values
    // will xor themselves out.
    let n : u32 = arr.len().try_into().expect("N was larger than a u32.");
    let mut tot : u32 = 0;
    for v in 1..n {
        tot = tot ^ v;
    }
    for v in arr {
        tot = tot ^ v;
    }
    tot
}

fn main() {
    let test = [1, 2, 2, 3, 4, 5];
    println!("Repeated value in {:?} is {}", test, pigeonhole2(&test[..]));
}
