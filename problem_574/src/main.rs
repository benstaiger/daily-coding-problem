
// This problem was asked by Amazon.
// 
// Implement a bit array.
// 
// A bit array is a space efficient array that holds a value of 1 or 0 at each index.
// 
// init(size): initialize the array with size
// set(i, val): updates index at i with val where val is either 1 or 0.
// get(i): gets the value at index i.

#[derive(Debug)]
struct BitArray {
    data: Vec<u32>,
}

impl BitArray {
    fn init(size: usize) -> BitArray {
        let num_u32 = if size % 32 == 0 { size / 32 } else { size / 32 + 1};
        BitArray { data: vec![0; num_u32] }
    }

    fn set(&mut self, i: usize, val: bool) {
        let idx = i / 32;
        let remainder = i % 32;
        if val {
            self.data[idx] = self.data[idx] | (1 << remainder);
        } else {
            let mask = (1 << remainder) ^ 0xFFFF;
            self.data[idx] = self.data[idx] & mask;
        }
    }

    fn get(&self, i: usize) -> bool {
        let idx = i / 32;
        let remainder = i % 32;
        (self.data[idx] & (1 << remainder)) != 0
    }
}

fn main() {
    let mut example = BitArray::init(60);
    example.set(10, true);
    example.set(11, true);
    example.set(60, true);
    for i in 0..60 {
        if i != 10 && i != 60 && i != 11{
            assert!(!example.get(i));
        } else {
            assert!(example.get(i));
        }
    }
    example.set(10, false);
    example.set(60, false);
    for i in 0..60 {
        if i != 11 {
            assert!(!example.get(i));
        } else {
            assert!(example.get(i));
        }
    }
}
