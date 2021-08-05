from functools import lru_cache


@lru_cache(None)  # unlimited cache size
# our cache will be at most O(N^2) in size where N is the number of operands
# since we will *atmost* store every sub-expression expression[i:j] for all
# i < j
def parenthesize_helper(expression):
    """
    This helper function determines how many ways there are to parenthesize
    a boolean expression by recursively constructing binary tree representation
    of the expression.

    For every operator we select it to be the root of the tree, then construct
    the all possible trees for the left and right expressions.

    This will result in the evaluation of all possible syntax trees. As we
    construct these trees, we propagate the number of True and False
    evaluations that are possible
    """
    if len(expression) <= 1:
        if expression == "T":
            return 0, 1
        elif expression == "F":
            return 1, 0
        else:
            raise ValueError(f"Unexpected single input {expression}")

    false_possibilities = 0
    true_possibilities = 0
    for i, v in enumerate(expression):
        if v in ["|", "&", "^"]:
            left_f, left_t = parenthesize_helper(expression[:i])
            right_f, right_t = parenthesize_helper(expression[i + 1 :])
            if v == "|":
                valid = left_t * right_t + left_t * right_f + left_f * right_t
                invalid = left_f * right_f
            elif v == "&":
                valid = left_t * right_t
                invalid = (
                    left_f * right_f + left_t * right_f + left_f * right_t
                )
            elif v == "^":
                valid = left_t * right_f + left_f * right_t
                invalid = left_t * right_t + left_f * right_f
            false_possibilities += invalid
            true_possibilities += valid
    return false_possibilities, true_possibilities


def parenthesize(expression):
    _, trues = parenthesize_helper(expression)
    return trues


def test_parenthesize():
    assert parenthesize("T") == 1
    assert parenthesize("F") == 0
    assert parenthesize("F|T") == 1
    assert parenthesize("F|F") == 0
    assert parenthesize("F&T") == 0
    assert parenthesize("F^T") == 1
    assert parenthesize("T|T|T") == 2
    assert parenthesize("T|T^T") == 1
    assert parenthesize("F|T&T") == 2
    try:
        parenthesize("|T&T") == 2
        assert False
    except ValueError:
        pass


if __name__ == "__main__":
    test_parenthesize()
