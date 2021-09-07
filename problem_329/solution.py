from copy import deepcopy
from itertools import chain
from collections import defaultdict

# This problem was asked by Amazon.
#
# The stable marriage problem is defined as follows:
#
# Suppose you have N men and N women, and each person has ranked their
# prospective opposite-sex partners in order of preference.
#
# For example, if N = 3, the input could be something like this:
#
# guy_preferences = {
#     'andrew': ['caroline', 'abigail', 'betty'],
#     'bill': ['caroline', 'betty', 'abigail'],
#     'chester': ['betty', 'caroline', 'abigail'],
# }
#
# gal_preferences = {
#     'abigail': ['andrew', 'bill', 'chester'],
#     'betty': ['bill', 'andrew', 'chester'],
#     'caroline': ['bill', 'chester', 'andrew']
# }
#
# Write an algorithm that pairs the men and women together in such a way that
# no two people of opposite sex would both rather be with each other than
# with their current partners.


def prefer(preferences, p1, p2):
    # Could be O(1) by changing the format of preferences to a map of ranks.
    if p2 is None:
        return True
    return preferences.index(p1) < preferences.index(p2)


def check_marriage(guys, gals, partners):
    for b in guys:
        for g in gals:
            if prefer(guys[b], g, partners[b]) and prefer(
                gals[g], b, partners[g]
            ):
                print(f"{b} and {g} would prefer to be together!")
                return False
    return True


def stable_marriage(guys, gals):
    _guys = {
        g: list(reversed(p)) for g, p in guys.items()
    }  # avoid changing input
    partners = {g: None for g in chain(_guys, gals)}
    men = [g for g in _guys]
    while men:
        guy = men.pop()
        while _guys[guy]:
            girl = _guys[guy].pop()
            if prefer(gals[girl], guy, partners[girl]):
                prev_partner = partners[girl]
                partners[girl] = guy
                partners[guy] = girl
                if prev_partner:
                    partners[prev_partner] = None
                    men.append(prev_partner)
                break

    return partners


def test_stable_marriage():
    guy_preferences = {
        "andrew": ["caroline", "abigail", "betty"],
        "bill": ["caroline", "betty", "abigail"],
        "chester": ["betty", "caroline", "abigail"],
    }
    gal_preferences = {
        "abigail": ["andrew", "bill", "chester"],
        "betty": ["bill", "andrew", "chester"],
        "caroline": ["bill", "chester", "andrew"],
    }
    partners = stable_marriage(guy_preferences, gal_preferences)
    assert check_marriage(guy_preferences, gal_preferences, partners)


if __name__ == "__main__":
    test_stable_marriage()
