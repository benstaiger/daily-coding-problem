import functools
import numpy as np


# You are given a list of data entries that represent entries and exits of
# groups of people into a building. An entry looks like this:
#
# {"timestamp": 1526579928, count: 3, "type": "enter"}
#
# This means 3 people entered the building. An exit looks like this:
#
# {"timestamp": 1526580382, count: 2, "type": "exit"}
#
# This means that 2 people exited the building. timestamp is in Unix time.
#
# Find the busiest period in the building, that is, the time with the most
# people in the building. Return it as a pair of (start, end) timestamps. You
# can assume the building always starts off and ends up empty, i.e. with 0
# people inside.


def busiest_time(logs):
    # Do the entries come in sorted order?
    # if yes, this is very trivial, if no, it take a bit more work.
    logs = sorted(logs, key=lambda x: x["timestamp"])
    values = [x["count"] * -1 if x["type"] == "exit" else 1 for x in logs]
    total_people = np.cumsum(values)
    peak_time = np.argmax(total_people)
    return logs[peak_time]["timestamp"], logs[peak_time+1]["timestamp"]


def busiest_time_not_sorted(logs):
    pass
