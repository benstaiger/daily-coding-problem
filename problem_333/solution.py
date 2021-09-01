
# This problem was asked by Pinterest.
#
# At a party, there is a single person who everyone knows, but who does not
# know anyone in return (the "celebrity"). To help figure out who this is, you
# have access to an O(1) method called knows(a, b), which returns True if
# person a knows person b, else False.
#
# Given a list of N people and the above operation, find a way to identify the
# celebrity in O(N) time.

# validating an individual as a celebrity takes O(N) time to confirm. Them
# / everyone who they know.
# marking someone as not a celebrity can take up to O(N) time.
# because we have to check that they know no one.


# If we had the information encoded in a better format, this problem would be
# trivial, but sampling the data requires O(N^2) to check all relationships

def adjacency_knows(a, b, edges):
    return (a, b) in edges


def check_celebrity(i, people, knows):
    return all([knows(j, i) and not knows(i, j) for j in people if j != i])


def find_celebrity_brute(people, knows):
    for i in people:
        if check_celebrity(i, people, knows):
            return i


def find_celebrity(people, knows):
    """
    We will run through each person eliminating them if they do not qualify
    as a celebrity.

    This will leave us with individuals who might be a celebrity, we will then
    validate those individuals.
    """
    people_stack = people.copy()
    while len(people_stack) > 1:
        i, j = people_stack.pop(), people_stack.pop()

        if knows(i, j):
            people_stack.append(j)
        elif knows(j, i):
            people_stack.append(i)
    if people_stack and check_celebrity(people_stack[0], people, knows):
        return people_stack[0]
     

def test_find_celebrity_simple():
    edges = {
        (0, 1),
        (0, 2),
        (0, 3),
        (2, 1),
        (2, 0),
        (3, 1),
        (3, 2),
    }
    people = list(range(4))
    assert find_celebrity(people, lambda a, b: adjacency_knows(a, b, edges)) == 1


def test_find_celebrity_missing():
    edges = {
        (0, 1),
        (0, 2),
        (0, 3),
        (2, 1),
        (2, 0),
        (3, 1),
        (3, 2),
    }
    people = list(range(4))
    edges.add((1, 0))  # 1 is no longer a celebrity
    assert find_celebrity(people, lambda a, b: adjacency_knows(a, b, edges)) is None


def test_find_celebrity_missing2():
    edges = {
        (0, 1),
        (1, 0),
        (1, 2),
        (2, 0),
    } # 1 is not actually a celebrity
    people = list(range(3))
    assert find_celebrity(people, lambda a, b: adjacency_knows(a, b, edges)) is None


if __name__ == "__main__":
    test_find_celebrity_simple()
    test_find_celebrity_missing()
    test_find_celebrity_missing2()
