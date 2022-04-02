fn rand_dist<T: Copy>(vals: &[T], probs: &[f32]) -> T {
    let cdf: Vec<f32> = probs
        .iter()
        .scan(0.0, |state, &x| {
            *state = *state + x;
            Some(*state)
        })
        .map(|x| x)
        .collect();

    let num: f32 = rand::random::<f32>();
    let idx = cdf.binary_search_by(|v| v.partial_cmp(&num).expect("cannot compare NAN"));
    let idx = match idx {
        Ok(v) => v,
        Err(v) => v,
    };
    println!("{:?} {} {}", cdf, num, idx);
    vals[idx]
}

fn main() {
    let cdf = rand_dist(&vec![1, 2, 3, 4], &vec![0.2, 0.3, 0.4, 0.1]);
    println!("cdf: {:?}", cdf);
}
