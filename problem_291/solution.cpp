#include <algorithm>
#include <iostream>
#include <vector>


int assignLifeRafts(std::vector<unsigned> weights, unsigned maxWeight) {
    std::sort(weights.begin(), weights.end());

    unsigned numBoats = 0;
    auto p1 = weights.begin();
    auto p2 = --weights.end();

    if (*p2 > maxWeight) {
        return -1;
    }
    while (p1 < p2) {
        if (*p1 + *p2 <= maxWeight) {  // put p1 and p2 on a boat together.
            ++numBoats;
            ++p1;
            --p2;
        } else {  // put p2 on a boat by themselves.
            ++numBoats;
            --p2;
        }
    }
    if (p1 == p2) {  // p1 has not yet been assigned a boat.
        ++numBoats;
    }
    return numBoats;
}


int main() {
    // check provided test case.
    std::cout << assignLifeRafts({100, 200, 150, 80}, 200) << std::endl;

    // check provided test case.
    std::cout << assignLifeRafts({100, 200, 200, 150, 80}, 200) << std::endl;

    // check that it works when everyone can share
    std::cout << assignLifeRafts({100, 50, 150, 80}, 200) << std::endl;

    // check that it works when someone doesn't fit.
    std::cout << assignLifeRafts({100, 240, 150, 80}, 200) << std::endl;

    // check that it when everyone needs their own raft.
    std::cout << assignLifeRafts({100, 120, 200}, 200) << std::endl;
}