import random


class Die:

    def __init__(self, num_sides=6):
        self._num_sides = num_sides

    def __add__(self, other):
        print("self's expected: {}".format(self.expected()))
        print("other's expected: {}".format(other.expected()))
        return self.expected() + other.expected()

    def roll(self):
        return random.randint(1, self._num_sides)

    def expected(self):
        return (self._num_sides + 1) / 2


class LoadedDie(Die):

    def roll(self):
        if random.randint(1, 2) == 2:  # 50% of the time
            return 1
        else:
            return random.randint(1, self._num_sides)
