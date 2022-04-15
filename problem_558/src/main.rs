use rand::prelude::*;

// This problem was asked by Google.
// 
// The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
// 
// Hint: The basic equation of a circle is x2 + y2 = r2.

fn in_circle(x: f64, y: f64, r: f64) -> bool {
    x*x + y*y < r*r
}

fn estimate_pi() -> f64 {
    // area of a square bounding a circle of radius r is (2*r)^2 = 4*r^2

    // for a circle of radius 1, the bounding square has side length 2 and area 4.
    let mut samples = 0.0;
    let mut num_in_circle = 0.0;
    let mut rng = rand::thread_rng();
    let mut estimate = 3.0;
    loop {
        let x: f64 = rng.gen();
        let y: f64 = rng.gen();
        samples += 1.0;
        if in_circle(x, y, 1.0) {
            num_in_circle += 1.0;
        }

        // could change break criteria to be dependent of the current estimate
        // rather than the number of sampled points.
        if samples > 1000000.0 {
            break;
        }
    }
    4.0 * num_in_circle / samples  // 4.0 is the area of a square with side length 2.
}

fn main() {
    println!("pi estimate = {}", estimate_pi());
}
