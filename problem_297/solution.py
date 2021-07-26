

# This problem was asked by Amazon.
#
# At a popular bar, each customer has a set of favorite drinks, and will
# happily accept any drink among this set. For example, in the following
# situation, customer 0 will be satisfied with drinks 0, 1, 3, or 6.
#
# preferences = {
#     0: [0, 1, 3, 6],
#     1: [1, 4, 7],
#     2: [2, 4, 7, 5],
#     3: [3, 2, 5],
#     4: [5, 8]
# }
# A lazy bartender working at this bar is trying to reduce his effort by
# limiting the drink recipes he must memorize. Given a dictionary input such
# as the one above, return the fewest number of drinks he must learn in order
# to satisfy all customers.
#
# For the input above, the answer would be 2, as drinks 1 and 5 will satisfy
# everyone.

def min_drinks_greedy(preferences):
    """
    This implements the set-cover greed approximation.

    This true solution to this problem requires us to implement a solution to
    the set-cover problem which is NP-complete.

    We successively add drinks that will satisfy the largest number of
    currently unsatisfied people.
    """
    drink_popularity = {}
    for person, drinks in preferences.items():
        for d in drinks:
            try:
                drink_popularity[d].add(person)
            except KeyError:
                drink_popularity[d] = set([person])

    drink_list = []

    while True:
        drinks = [(len(drink_popularity[d]), d) for d in drink_popularity.keys()]
        drinks = sorted(drinks, reverse=True)

        happy_people, best_drink = drinks[0]
        if happy_people == 0:
            break

        drink_list.append(best_drink)
        to_remove = drink_popularity[best_drink].copy()
        for d in drink_popularity.keys():
            drink_popularity[d] -= to_remove

    return drink_list


def test_min_drinks():
    preferences = {
        0: [0, 1, 3, 6],
        1: [1, 4, 7],
        2: [2, 4, 7, 5],
        3: [3, 2, 5],
        4: [5, 8]
    }
    print(min_drinks_greedy(preferences))


if __name__ == "__main__":
    test_min_drinks()
