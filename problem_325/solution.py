
# This problem was asked by Jane Street.
#
# The United States uses the imperial system of weights and measures, which
# means that there are many different, seemingly arbitrary units to measure
# distance. There are 12 inches in a foot, 3 feet in a yard, 22 yards in a
# chain, and so on.
#
# Create a data structure that can efficiently convert a certain quantity of
# one unit to the correct amount of any other unit. You should also allow for
# additional units to be added to the system.


class Distance:
    ratios = {
        "Inch": 1,
        "Foot": 12,
        "Yard": 36,
        "Chain": 36*22,
        } 

    def __init__(self, distance, unit="Inch"):
        self.value = distance * Distance.ratios[unit]

    @classmethod
    def add_unit(cls, name: str, num_of_inches: float):
        if name in cls.ratios:
            raise KeyError("Unit name already exists!")
        else:
            cls.ratios[name] = num_of_inches
            # We could even add a generator to produce classes of each name

    def get_distance(self, unit: str):
        return self.value / Distance.ratios[unit]


def test_Distance_conversion():
    d1 = Distance(1) 
    d2 = Distance(1, "Yard")
    assert d1.get_distance("Inch") == 1
    assert d1.get_distance("Yard") == 1/36
    assert d2.get_distance("Inch") == 36
    assert d2.get_distance("Yard") == 1
    assert d2.get_distance("Foot") == 3


def test_Distance_add_unit():
    d1 = Distance(1, "Inch") 
    Distance.add_unit("Test", 6)
    assert d1.get_distance("Test") == 1/6
    try:
        d1.add_unit("Inch", 2)
        assert False
    except KeyError:
        pass


if __name__ == "__main__":
    test_Distance_conversion()
    test_Distance_add_unit()

