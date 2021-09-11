from collections import defaultdict
import heapq

# This problem was asked by Airbnb.
#
# You are given a huge list of airline ticket prices between different cities
# around the world on a given day. These are all direct flights. Each element
# in the list has the format (source_city, destination, price).
# 
# Consider a user who is willing to take up to k connections from their origin
# city A to their destination B. Find the cheapest fare possible for this
# journey and print the itinerary for that journey.
#
# For example, our traveler wants to go from JFK to LAX with up to 3
# connections, and our input flights are as follows:
#
# [
#     ('JFK', 'ATL', 150),
#     ('ATL', 'SFO', 400),
#     ('ORD', 'LAX', 200),
#     ('LAX', 'DFW', 80),
#     ('JFK', 'HKG', 800),
#     ('ATL', 'ORD', 90),
#     ('JFK', 'LAX', 500),
# ]
# Due to some improbably low flight prices, the cheapest itinerary would be
# JFK -> ATL -> ORD -> LAX, costing $440.


def plan_trip_bfs(from_city, to_city, connections, flights):
    # O(E*k)
    edges = defaultdict(list)
    for a1, a2, cost in flights:
        edges[a1].append((cost, a2))

    stack = [e for e in edges[from_city]]

    cheapest = float('inf')
    path = []
    for i in range(connections):
        new_stack = []
        while stack:
            cost, city = stack.pop()
            if city == to_city and cost < cheapest:
                cheapest = cost
            else:
                for price, city2 in edges[city]:
                    if cost + price < cheapest:
                        new_stack.append((cost + price, city2))
        stack = new_stack

    return cheapest


def plan_trip_dijkstra(from_city, to_city, connections, flights):
    # O(E + VlogV)
    edges = defaultdict(list)
    for a1, a2, cost in flights:
        edges[a1].append((cost, a2))

    heap = [(cost, 1, city) for cost, city in edges[from_city]]
    heapq.heapify(heap)

    cheapest = float('inf')
    path = []
    airport_cost = [float("inf") for a in edges]
    airport_cost[from_city] = 0

    while heap:
        cost, step, city = heapq.heappop(heap)
        if cost <= airport_cost[city2]:
            continue  # only continue search if it is the shortest known path
        if city == to_city:
            cheapest = cost
            break
        elif step < connections:
            for price, city2 in edges[city]:
                if cost + price < airport_cost[city2]:
                    heapq.heappush(heap, (cost + price, step+1, city2))

    return cheapest


def test_plan_trip(alg):
    flights = [
        ('JFK', 'ATL', 150),
        ('ATL', 'SFO', 400),
        ('ORD', 'LAX', 200),
        ('LAX', 'DFW', 80),
        ('JFK', 'HKG', 800),
        ('ATL', 'ORD', 90),
        ('JFK', 'LAX', 500),
    ]
    assert alg("JFK", "LAX", 3, flights) == 440


def test_plan_trip_bfs():
    test_plan_trip(plan_trip_bfs)


def test_plan_trip_dijkstra():
    test_plan_trip(plan_trip_dijkstra)


if __name__ == "__main__":
    test_plan_trip_bfs()
    test_plan_trip_dijkstra()

