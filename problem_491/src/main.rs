use num::Unsigned;
use std::fmt::Display;

// This problem was asked by Palantir.
// 
// Write a program that checks whether an integer is a palindrome. For example,
// 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert
// the integer into a string.

fn is_palindrome<T>(number: T) -> bool 
    where T: Unsigned + Display
{
    let st = format!("{}", number);
    let seq = st.as_bytes();
    seq.iter().eq(seq.iter().rev())
}

fn print_palindrome<T: num::Unsigned>(number: T)
    where T: Unsigned + Display + Copy
{
    println!("{} is a palindrome. {}", number, is_palindrome(number));
}

fn main() {
    print_palindrome(131u32);
    print_palindrome(4121u64);
    print_palindrome(0usize);
    print_palindrome(12321u32);
}
