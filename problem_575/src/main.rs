// This problem was asked by Uber.
//
// Implement a 2D iterator class. It will be initialized with an array of
// arrays, and should implement the following methods:
//
// next(): returns the next element in the array of arrays. If there are no
// more elements, raise an exception.
// has_next(): returns whether or not the iterator still has elements left.
// For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next()
// repeatedly should output 1, 2, 3, 4, 5, 6.
//
// Do not use flatten or otherwise clone the arrays. Some of the arrays can be
// empty.

struct Iter2D {
    data: Vec<Vec<i32>>,
    array_num: usize, // [num][idx] will always point to the next element.
    array_idx: usize, // if there are no more elements, num will be past end.
}

impl Iter2D {
    fn new(data: Vec<Vec<i32>>) -> Iter2D {
        let array_idx = 0;
        let mut array_num = 0;
        while array_num < data.len() && data[array_num].len() == 0 {
            array_num += 1
        }
        Iter2D {
            data,
            array_num,
            array_idx,
        }
    }

    fn has_next(&self) -> bool {
        self.array_num < self.data.len()
    }
}

impl Iterator for Iter2D {
    type Item = i32;

    fn next(&mut self) -> Option<Self::Item> {
        if self.has_next() {
            let res = self.data[self.array_num][self.array_idx];
            if self.array_idx + 1 < self.data[self.array_num].len() {
                self.array_idx += 1;
            } else {
                self.array_idx = 0;
                self.array_num += 1;
                while self.array_num < self.data.len() && self.data[self.array_num].len() == 0 {
                    self.array_num += 1
                }
            }

            Some(res)
        } else {
            None
        }
    }
}

fn main() {
    let example: Vec<Vec<i32>> = vec![
        vec![1, 2],
        vec![],
        vec![3],
        vec![4, 5, 6],
        vec![],
        vec![],
    ];
    for v in Iter2D::new(example) {
        println!("{}", v);
    }
}
