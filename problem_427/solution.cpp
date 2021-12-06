#include <algorithm>
#include <iostream>
#include <numeric>
#include <queue>
#include <unordered_map>
#include <vector>

// This problem was asked by Square.
// 
// A competitive runner would like to create a route that starts and ends at
// his house, with the condition that the route goes entirely uphill at first,
// and then entirely downhill.
// 
// Given a dictionary of places of the form {location: elevation}, and a
// dictionary mapping paths between some of these locations to their
// corresponding distances, find the length of the shortest route satisfying
// the condition above. Assume the runner's home is location 0.
// 
// For example, suppose you are given the following input:
// 
// elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
// paths = {
//     (0, 1): 10,
//     (0, 2): 8,
//     (0, 3): 15,
//     (1, 3): 12,
//     (2, 4): 10,
//     (3, 4): 5,
//     (3, 0): 17,
//     (4, 0): 10
// }
// In this case, the shortest valid path would be 0 -> 2 -> 4 -> 0, with a
// distance of 28.

struct PairHash {
    template <class T1, class T2>
    std::size_t operator () (const std::pair<T1,T2> &p) const {
        auto h1 = std::hash<T1>{}(p.first);
        auto h2 = std::hash<T2>{}(p.second);

        // Mainly for demonstration purposes, i.e. works but is overly simple
        // In the real world, use sth. like boost.hash_combine
        // Should work fine for this simple example where nothing will
        // have a symmetric pair.
        return h1 ^ h2;  
    }
};


// Use a modified Dijkstra's algorithm to find the shortest path subject
// to the hill-climbing constraint.
std::vector<int> findShortestHill(
        std::unordered_map<std::pair<int, int>, int, PairHash> paths,
        std::vector<int> elevation) {

    // (dist, from, to, ascending)
    using PathType = std::tuple<int, int, int, bool>;

    // from: (to, dist)
    std::vector<std::vector<std::pair<int, int>>> edges(elevation.size());
    for (const auto& [p, dist] : paths) {
        const auto [from, to] = p;
        edges[from].emplace_back(to, dist);  // default construct vect on first access
    }

    std::priority_queue<PathType, std::vector<PathType>, std::greater<PathType>> closest;
    std::vector<int> dists(elevation.size(), std::numeric_limits<int>::max());
    // initial search with all nodes adjacent to the start
    for (const auto& [to, dist] : edges[0]) {
        // We can't start by going down.
        if (elevation[to] >= elevation[0]) {
            closest.emplace(dist, 0, to, true);
            dists[to] = dist;
        }
    }

    std::vector<int> shortest(elevation.size());
    // From a given point, we will continue our search along any node that
    // hasn't been seen yet and:
    //  a) continues upward, if we're still going up
    //  b) goes downward if we're going down
    while (closest.size() > 0) {
        const auto [dist, from, to, ascending] = closest.top();
        closest.pop();

        if (to == 0) {  // short-circuit since this is all we care about.
            shortest[to] = from;
            break;
        }
        if (dists[to] == dist) {  // shortest path to the node.
            shortest[to] = from;

            for (const auto& [to_next, dist_next] : edges[to]) {
                const int total_dist = dist + dist_next;
                if (dists[to_next] > total_dist) {
                    dists[to_next] = total_dist;
                    if (ascending && elevation[to_next] >= elevation[to]) {
                        closest.emplace(total_dist, to, to_next, true);
                    } else if (elevation[to_next] < elevation[to]) {
                        closest.emplace(total_dist, to, to_next, false);
                    }
                }
            }
        }
    }
    std::vector<int> res;
    res.push_back(0);
    int pos = shortest[0];
    while (pos != 0) {
        res.push_back(pos);
        pos = shortest[pos];
    }
    res.push_back(pos);
    std::reverse(res.begin(), res.end());
    return res;
}


void testPathFinding() {
    std::vector<int> elevation{
        5, 25, 15, 20, 10
    };
    using FromTo = std::pair<int, int>;
    std::unordered_map<FromTo, int, PairHash> paths{
        {{0, 1}, 10},
        {{0, 2}, 8},
        {{0, 3}, 15},
        {{1, 3}, 12},
        {{2, 4}, 10},
        {{3, 4}, 5},
        {{3, 0}, 17},
        {{4, 0}, 10}
    };
    std::vector<int> shortest = findShortestHill(paths, elevation);
    assert(shortest.size() == 4);
    assert(shortest[0] == 0);
    assert(shortest[1] == 2);
    assert(shortest[2] == 4);
    assert(shortest[3] == 0);
}


int main() {
    testPathFinding();
    return 0;
}