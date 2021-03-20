import os
import sys
import pytest


if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath(os.path.join(
        os.path.dirname(__file__), os.pardir, os.pardir)))


from problem_171.problem_171 import busiest_time


def test_simple_example():
    example = [
        {"timestamp": 728, "count": 3, "type": "enter"},
        {"timestamp": 932, "count": 2, "type": "exit"},
        {"timestamp": 933, "count": 1, "type": "exit"},
    ]
    start_peak, end_peak = busiest_time(example)
    assert (start_peak == 728 and end_peak == 932)


def test_simple_unsorted():
    example = [
        {"timestamp": 932, "count": 2, "type": "exit"},
        {"timestamp": 728, "count": 3, "type": "enter"},
        {"timestamp": 932, "count": 1, "type": "exit"},
    ]
    start_peak, end_peak = busiest_time(example)
    assert (start_peak == 728 and end_peak == 932)


# Questions not answered by ther prompt:
#   what happens if there are multiple log entries at the same moment?
#   what happens if there are multiple time points with the same, max values
#   do the entries have to be sorted?


if __name__ == "__main__":
    pytest.main()
