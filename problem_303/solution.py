import datetime

# This problem was asked by Microsoft.
#
# Given a clock time in hh:mm format, determine, to the nearest degree, the
# angle between the hour and the minute hands.


def time_angle(t: datetime.time):
    hours = t.hour if t.hour < 12 else t.hour - 12
    total_mins = hours * 60 + t.minute

    degree_hour_angle = total_mins / (60 * 12) * 360
    degree_minute_angle = t.minute / 60 * 360

    angle = abs(round(degree_hour_angle - degree_minute_angle))
    return min(angle, 360 - angle)


def test_time_angle():
    assert time_angle(datetime.time(0, 0)) == 0
    assert time_angle(datetime.time(12, 0)) == 0
    assert time_angle(datetime.time(3, 0)) == 90
    assert time_angle(datetime.time(6, 0)) == 180
    assert time_angle(datetime.time(9, 0)) == 90
    print(time_angle(datetime.time(12, 30)))
    assert (
        time_angle(datetime.time(12, 30)) > 160
        and time_angle(datetime.time(12, 30)) < 180
    )


if __name__ == "__main__":
    test_time_angle()
