#include <string>
#include <unordered_map>
#include <vector>

// This problem was asked by Facebook.
// 
// Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count
// the number of ways it can be decoded.
// 
// For example, the message '111' would give 3, since it could be decoded as
// 'aaa', 'ka', and 'ak'.
// 
// You can assume that the messages are decodable. For example, '001' is not
// allowed.

// We will solve this as a dynamic programming question
// for each value we can either take it as an individual new character (maybe)
// or combined with the previous value. We can then accumulate the total
// number of possible encodings up to any point in the sequence.

size_t numSequences(const std::vector<unsigned>& sequence, const std::unordered_map<int, char>& mapping) {
    std::vector<size_t> possibilities(sequence.size(), 0);
    possibilities[0] = 1;
    for (size_t pos = 1; pos < sequence.size(); ++pos) {
        // treat sequence[pos] independent of the prev value
        if (sequence[pos] > 0) {
            possibilities[pos] += possibilities[pos-1];
        }

        // treat it in conjunction with the previous value.
        const int val = sequence[pos-1]*10 + sequence[pos];
        // check that it is a valid 2-character sequence. We could check this in the map.
        if (sequence[pos-1] > 0 && val > 0 && val <= 26) {
            if (pos == 1) {
                possibilities[pos] += 1;
            } else {
                possibilities[pos] += possibilities[pos-2];
            }
        }
    }

    return possibilities.back();
}

int main() {
    std::unordered_map<int, char> map;
    std::vector<unsigned> seq {{
        1u, 1u, 1u, 1u
    }};
    // aaaa, aak, aka, kaa, kk
    assert(numSequences(seq, map) == 5);
}