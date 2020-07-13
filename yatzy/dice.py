import random
import attr


@attr.s
class Die:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError("Must have at least 2 sides.")
        if not isinstance(sides, int):
            raise ValueError("Sides must be a whole number")
        if not isinstance(value, int):
            raise ValueError("Value must be whole numbers")
        self.value = value or random.randint(1, sides)

    # return as int
    def __int__(self):
        return self.value

    # return the equal
    def __eq__(self, other):
        return int(self) == other

    # return greater than
    def __gt__(self, other):
        return int(self) > other

    # return less than
    def __lt__(self, other):
        return int(self) < other

    # return greater or equal
    def __ge__(self, other):
        return int(self) > other or int(self) == other

    # return less or equal
    def __le__(self, other):
        return int(self) < other or int(self) == other

    # return the addition
    def __add__(self, other):
        return int(self) + other

    # return the addition reversed
    def __radd__(self, other):
        return int(self) + other


@attr.s
class D6(Die):
    def __init__(self, value=0):
        # whatever magic method I want to overwrite is preceded with super() in the subclass
        super().__init__(sides=6, value=value)
