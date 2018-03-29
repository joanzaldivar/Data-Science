#put all dice in bag
#bag = [4,6,6,8,8,8,8,10,10,12,20,20,20]

#functions
#Do these steps twice for first round
#dice_sides = get_dice_type(dice_type)
    #returns a random index from bag
#dice_face = get_dice_face(dice_type)
    #return a random face from that dice based on number of sides
#total = get_dice_face_sum(dice_face)
#reduce_dice_count(dice_sides)
    # remove the dice from the bag with that # of sides

#Do these steps thrice for second round
#dice_sides = get_dice_type(dice_type)
    #returns a random index from dice
#dice_face = get_dice_face(dice_type)
    #return a random face from that dice based on number of sides
#total = get_dice_face_sum(dice_face)
#reduce_dice_count(dice_sides)
    # remove the dice from the bag with that # of sides

import random

class Die:
    def __init__(self, num_sides=6):
        # Input validation
        if num_sides > 20:
            raise ValueError("you can't have more than 20 sides on a die")

        # State management
        self._num_sides = num_sides

        # Alternate state management
        self._faces = range(1, num_sides + 1)

    def roll(self):
        return random.randint(1, self._num_sides)

    def alt_roll(self):
        return random.choice(self._faces)

class Bag:
    def __init__(self, dice_dictionary):
        self.bag = []
        for sides, count in dice_dictionary.items():
            for _ in range(count):
                self.bag.append(Die(num_sides=sides))
        #this builds a list like
        #bag = [4, 6, 6, 8, 8, 8, 8, 10, 10, 12, 20, 20, 20]

    def draw(self, num_things=1):
        drawn = []
        for _ in range(num_things):
            random.shuffle(self.bag)
            popped = self.bag.pop()
            drawn.append(popped)
            print(popped)

        return drawn

if __name__ == '__main__':
    b = Bag({4:1, 6:2, 8:4, 10:2, 12:1, 20:3})
    set_aside = b.draw(num_things=3)
    drawn = b.draw(num_things=2)
    s = sum([die.roll() for die in drawn])
    print(s)