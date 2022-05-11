
// This problem was asked by Spotify.
// 
// Write a function, throw_dice(N, faces, total), that determines how many ways
// it is possible to throw N dice with some number of faces each to get a
// specific total.
// 
// For example, throw_dice(3, 6, 7) should equal 15.

fn throw_dice(n: u32, faces: u32, target: u32) -> Vec<Vec<u32>> {
    assert!(target > 0);
    if n == 1 {
        if target <= faces {
            return vec![vec![target]];
        } else {
            return Vec::new();
        }
    }
    let mut possibilities = Vec::new();
    for i in 1..=faces {
        if target > i {
            // We would want to memoize this solution.
            let rets = throw_dice(n - 1, i, target-i);
            if rets.len() > 0 {
                for mut v in rets.into_iter() {
                    v.push(i);
                    possibilities.push(v);
                }
            }
        }
    }

    return possibilities;
}

fn main() {
    // This solution omits permutations of the dice.
    println!("3, 6, 7: {:?}", throw_dice(3, 6, 7));
    println!("2, 6, 7: {:?}", throw_dice(2, 6, 7));
}
