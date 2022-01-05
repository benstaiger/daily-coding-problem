#include <iostream>
#include <unordered_set>
#include <string>
#include <vector>

// This problem was asked by Google.
// 
// Given a word W and a string S, find all starting indices in S which are
// anagrams of W.
// 
// For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.

bool IsAnagram(std::string_view word1, std::string_view word2) {
    // O(N1 + N2)
    if (word1.size() != word2.size()) return false;
    std::unordered_multiset<char> letters1{word1.begin(), word1.end()};
    std::unordered_multiset<char> letters2{word2.begin(), word2.end()};
    return letters1 == letters2;
}

std::vector<size_t> AnagramsSimple(std::string_view word, std::string_view sequence) {
    std::vector<size_t> positions;
    for (size_t i = 0; i < (sequence.size() - word.size() + 1); ++i) {
        if (IsAnagram(word, sequence.substr(i, word.size()))) {
            positions.push_back(i);
        }
    }
    return positions;
}


std::ostream& operator<<(std::ostream& stream, const std::unordered_multiset<char>& iterable) {
    bool first = true;
    stream << "[";
    for (const auto& a : iterable) {
        if (first) {
            stream << a;
            first = false;
        } else {
            stream << ", " << a;
        }
    }
    stream << "]";
    return stream;
}


std::vector<size_t> AnagramsRolling(std::string_view word, std::string_view sequence) {
    if (sequence.size() < word.size()) return {};
    std::vector<size_t> positions;
    const std::unordered_multiset<char> wordLetters(word.begin(), word.end());
    std::unordered_multiset<char> remainingLetters{wordLetters};
    
    for (size_t i = 0; i < sequence.size(); ++i) {
        // identify if the letter is part of the remaining anagram letters
        auto pos = remainingLetters.find(sequence[i]);
        if (pos != remainingLetters.end()) {
            remainingLetters.erase(pos);
        } 

        // identify if seq (i-K, i]
        if (remainingLetters.size() == 0) {
            positions.push_back(i + 1 - word.size());
        }

        // re-add letters that are leaving the sliding window.
        if (i >= (word.size() - 1)) {
            const char leaving = sequence[i + 1 - word.size()];
            auto pos = wordLetters.find(leaving);
            if (pos != wordLetters.end() && wordLetters.count(leaving) > remainingLetters.count(leaving)) {
                remainingLetters.insert(leaving);
            }
        }
        assert(remainingLetters.size() <= word.size());
    }
    return positions;
}

std::vector<size_t> Anagrams(std::string_view word, std::string_view sequence) {
    return AnagramsRolling(word, sequence);
}

int main() {
    std::string sequence{"abbxaba"};
    std::string word{"ab"};
    const auto res = Anagrams(word, sequence);
    for(const auto r : res) {
        std::cout << r << " ";
    }
    std::cout << std::endl;
    assert(res.size() == 3);
    assert(res[0] == 0);
    assert(res[1] == 4);
    assert(res[2] == 5);
}