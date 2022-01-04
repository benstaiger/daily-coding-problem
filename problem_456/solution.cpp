#include <algorithm>
#include <iostream>
#include <tuple>
#include <vector>

// This problem was asked by Amazon.
// 
// You are given a list of data entries that represent entries and exits of
// groups of people into a building. An entry looks like this:
// 
// {"timestamp": 1526579928, count: 3, "type": "enter"}
// 
// This means 3 people entered the building. An exit looks like this:
// 
// {"timestamp": 1526580382, count: 2, "type": "exit"}
// 
// This means that 2 people exited the building. timestamp is in Unix time.
// 
// Find the busiest period in the building, that is, the time with the most
// people in the building. Return it as a pair of (start, end) timestamps.
// You can assume the building always starts off and ends up empty, i.e. with
// 0 people inside.


struct Entry {
    unsigned long timestamp;
    unsigned count;
    bool entering;
};

std::ostream& operator<<(std::ostream& stream, const Entry& entry) {
    stream << "{timestamp=" << entry.timestamp;
    stream << ", count=" << entry.count;
    stream << ", entering=" << entry.entering << "}";
    return stream;
}

bool operator<(const Entry& lhs, const Entry& rhs) {
    if (lhs.timestamp < rhs.timestamp) return true;
    if (rhs.timestamp < lhs.timestamp) return false;

    if (lhs.count < rhs.count) return true;
    if (rhs.count < lhs.count) return false;

    // kind people hold the door for those leaving.
    if (lhs.entering && !rhs.entering) return true;
    if (rhs.entering && !lhs.entering) return false;

    return false;
}

std::pair<unsigned long, unsigned long> BusiestPeriodSorted(const std::vector<Entry>& log) {
    std::pair<unsigned long, unsigned long> busiest;
    unsigned total = 0;
    unsigned max = 0;
    for (const auto& entry : log) {
        if (total == max) {
            busiest.second = entry.timestamp;
        }
        if (entry.entering) {
            total += entry.count;
        } else {
            if (entry.count > total) {
                throw std::domain_error("Total people in building is < 0.");
            }
            total -= entry.count;
        }
        if (total > max) {
           busiest.first = entry.timestamp; 
           max = total;
        }
    }
    return busiest;
}

std::pair<unsigned long, unsigned long> BusiestPeriod(const std::vector<Entry>& log) {
    if (!std::is_sorted(log.begin(), log.end())) {
        auto logCopy{log};
        std::sort(logCopy.begin(), logCopy.end());
        return BusiestPeriodSorted(logCopy);
    }
    return BusiestPeriodSorted(log);
}

int main() {
    const bool enter = true;
    const bool exit = false;
    std::vector<Entry> example {
        {1ul, 3u, enter},
        {2ul, 1u, exit},
        {3ul, 6u, enter},
        {4ul, 7u, exit},
        {5ul, 1u, exit}
    };
    const auto [start, stop] = BusiestPeriod(example);
    assert(start == 3);
    assert(stop == 4);
}