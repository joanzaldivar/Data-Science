import random

# Nouns: dice, bag, game, turn
# Verbs: roll, draw, summing


class Die:

    def __init__(self, num_sides=6):
        # Input validation
        if num_sides > 20:
            raise ValueError("you can't have more than 20 sides on a die, silly!")
        if num_sides % 2 != 0:
            raise ValueError("You can't have an odd-sided die")

        # State management
        self._num_sides = num_sides

    def __str__(self):
        return "a Die with {} sides".format(self._num_sides)

    def roll(self):
        return random.randint(1, self._num_sides)


class Bag:

    def __init__(self, dice_dictionary):
        self.bag = []
        for sides, count in dice_dictionary.items():
            for _ in range(count):
                self.bag.append(Die(num_sides=sides))

    def draw(self, num_things=1):
        drawn = []
        for _ in range(num_things):
            random.shuffle(self.bag)
            popped = self.bag.pop()
            drawn.append(popped)
        return drawn


if __name__ == '__main__':
    b = Bag(dice_dictionary={4: 1, 6: 2, 8: 4, 10: 2, 12: 1, 20: 3})
    set_aside = b.draw(num_things=3)
    drawn = b.draw(num_things=2)
    s = sum([die.roll() for die in drawn])
    print("We drew {} and the sum is: {}".format([str(d) for d in drawn], s))
