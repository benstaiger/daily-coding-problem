// This problem was asked by Palantir.
// 
// The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one. For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.
// 
// Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.


fn frac_sub(f1: (u64, u64), f2: (u64, u64)) -> (u64, u64) {
    (f1.0 * f2.1 - f2.0 * f1.1, f1.1 * f2.1)
}

fn find_egyption(frac: (u64, u64)) -> Vec<(u64, u64)> {
    let mut frac = frac;
    let mut result: Vec<(u64, u64)> = Vec::new();
    while frac.0 > 0 {
        let a = frac.0;
        let b = frac.1;
        // we know that b' = (floor(b / a) + b % a) is divisible by a by definition of division.
        // b' >= b.
        let bp = b/a + b%a;
        result.push((1, bp));
        frac = frac_sub(frac, (1, bp));
    }
    result
}

fn main() {
    let test = (4, 13);
    println!("Egyption of {:?} is {:?}", test, find_egyption(test));
}
