#include <cassert>
#include <string>
#include <vector>

// This problem was asked by Dropbox.
// 
// Implement an efficient string matching algorithm.
// 
// That is, given a string of length N and a pattern of length k, write a
// program that searches for the pattern in the string with less than O(N * k)
// worst-case time complexity.
// 
// If the pattern is found, return the start index of its location. If not,
// return False.

// This is just a question to implement KMP.

std::vector<int> kmpRestart(std::string_view pattern) {
    std::vector<int> restart(pattern.size(), -1);
    
    // for each position, i, find if the suffix of pattern[0 to i] is a prefix
    // to the pattern. If so, we can skip iterating over some elements.

    // -1 means that we didn't match any prefix with this letter. so we should
    // restart our search at the next position in the word.

    // >0 means we should check again with the letter in that position of the
    // pattern.

    //  a  a  a
    // -1 -1 -1

    //  a  b  a
    // -1  0 -1

    int pos = 1;
    int prefixPos = 0;
    while (pos < pattern.size()) {
        if (pattern[pos] == pattern[prefixPos]) {
            restart[pos] = restart[prefixPos];
        } else {
            restart[pos] = prefixPos;
            while (prefixPos >=0 && pattern[pos] != pattern[prefixPos]) {
                prefixPos = restart[prefixPos];
            }
        }
        ++pos;
        ++prefixPos;
    }
    return restart;
}

bool kmp(std::string_view str, std::string_view pattern) {
    // iterate through the str and the pattern at the same time
    // if we no longer match, we go back in the pattern based on where we
    // were when we failed the pattern match.
    const auto restart = kmpRestart(pattern);

    int patternPos = 0;
    int strPos = 0;
    while (strPos < str.size()) {
        if (str[strPos] == pattern[patternPos]) {
            ++patternPos;
            ++strPos;
            if (patternPos == pattern.size()) { return true; }
        } else {
            patternPos = restart[patternPos];
            if (patternPos < 0) {
                ++strPos;
                ++patternPos;
            }
        }
    }
    return false;
}

int main() {
    assert(kmp("somabaethabababaing", "ababa"));
}