
# This problem was asked by Microsoft.
# 
# You are given an string representing the initial conditions of some dominoes. Each element can take one of three values:
# 
# * L, meaning the domino has just been pushed to the left,
# * R, meaning the domino has just been pushed to the right, or
# * ., meaning the domino is standing still.
# Determine the orientation of each tile when the dominoes stop falling. Note that if a domino receives a force from the left and right side simultaneously, it will remain upright.
# 
# For example, given the string .L.R....L, you should return LL.RRRLLL.
# 
# Given the string ..R...L.L, you should return ..RR.LLLL.


def topple_dominos(initial_position):
    count = 0
    last_action = '.'
    new_state = list(initial_position)
    for i, s in enumerate(initial_position):
        if s == '.':
            if last_action == 'L':
                count += 1
            if last_action == 'R':
                count += 1
                new_state[i] = 'R'
            elif last_action in ['L', '.']:
                count += 1
        elif s == 'R':
            count = 0
            last_action = 'R'
        elif s == 'L': 
            if last_action == 'R':
                # backtrack to adjust
                for i2 in range(1, count//2 + 1):
                    new_state[i - i2] = 'L'
                if count % 2 == 1:
                    new_state[i - count//2 - 1] = '.'
            elif last_action in ['L', '.']:
                for i2 in range(1, count + 1):
                    new_state[i - i2] = 'L'
            count = 0
            last_action = 'L'
    return ''.join(new_state)


def test_topple_dominos():
    example = '..R...L.L'
    assert topple_dominos(example) == '..RR.LLLL'
    example = '..R....L.L'
    assert topple_dominos(example) == '..RRRLLLLL'
    example = '..L..R....L.L'
    assert topple_dominos(example) == 'LLL..RRRLLLLL'
    example = '..L..R....L.L.'
    assert topple_dominos(example) == 'LLL..RRRLLLLL.'
    example = '..L..R....L.L.R.'
    assert topple_dominos(example) == 'LLL..RRRLLLLL.RR'
    example = '..RR...L.L.'
    assert topple_dominos(example) =='..RRR.LLLL.' 


if __name__ == "__main__":
    test_topple_dominos()

