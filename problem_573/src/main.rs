use std::collections::VecDeque;

// This problem was asked by Google.
// 
// Given a stack of N elements, interleave the first half of the stack with the
// second half reversed using only one other queue. This should be done
// in-place.
// 
// Recall that you can only push or pop from a stack, and enqueue or dequeue
// from a queue.
// 
// For example, if the stack is [1, 2, 3, 4, 5], it should become
// [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].
// 
// Hint: Try working backwards from the end state.

// [1, 2, 3, 4, 5, 6]
// ->
// [1, 6, 2, 5, 3, 4]

// [1, 2, 3] | [4, 5, 6]
// [1, 2, 3] | [6, 5, 4] (reverse second half)
// interleave
// [1, 2] | [3, 4, 6, 5]
// [1] | [2, 5, 3, 4, 6]
// [] | [1, 6, 2, 5, 3, 4]
// push to stack
// [4, 3, 5, 2, 6, 1] | []
// push to queue and back to stack
// [1, 6, 2, 5, 3, 4]


// [1, 2, 3] | [5, 4]
// [1, 2] | [3, 4, 5]
// [1] | [2, 5, 3, 4]

// []


fn interleave_stack(mut stack: Vec<i32>) -> Vec<i32> {
    // we will leave the last element on the stack if it is odd.

    if stack.len() <= 1 {
        return stack;
    }
    let mut queue = VecDeque::new(); 
    let odd = stack.len() % 2 == 1;
    // First pop half the stack into the queue
    while stack.len() - 1 > queue.len() {
        queue.push_front(stack.pop().unwrap());
    }
    // Reverse the queue
    while queue.len() > 0 {
        stack.push(queue.pop_back().unwrap());
    }
    while stack.len() - 1 > queue.len() {
        queue.push_front(stack.pop().unwrap());
    }

    // Alternate pushing items from the front of the queue and the stack into
    // the back of the queue
    while stack.len() > if odd { 1 } else { 0 } {
        let back_item = queue.pop_back().unwrap();
        let front_item = stack.pop().unwrap();
        if odd {
            queue.push_front(front_item);
            queue.push_front(back_item);
        } else {
            queue.push_front(back_item);
            queue.push_front(front_item);
        }
    }

    // Drain the queue into the stack then reverse
    while queue.len() > 0 {
        stack.push(queue.pop_back().unwrap());
    }
    while stack.len() > if odd { 1 } else { 0 } {
        queue.push_front(stack.pop().unwrap());
    }
    while queue.len() > 0 {
        stack.push(queue.pop_back().unwrap());
    }
    stack
}

fn main() {
    println!("{:?}", interleave_stack(vec![1, 2, 3, 4, 5, 6]));
    println!("{:?}", interleave_stack(vec![1, 2, 3, 4, 5]));
}
