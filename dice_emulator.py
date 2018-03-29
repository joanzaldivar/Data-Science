"""Emulation is a good way to double-check theory.
If you could throw a pair of dice a great number of times,
the results should converge on the right answer.
But doing this manually would be quite tedious. So...

Write a Python program that estimates the
probability of rolling a given number on two dice.
Experiment with different numbers of rolls.
How many rolls are needed before you “trust” the emulation?"""

import random

rolls = int(input('# of rolls: '))
num = int(input('Outcome I want: '))
ctr = 0

for x in range(rolls):
    outcome = random.randint(1,6) + random.randint(1,6)
    if outcome == num:
        ctr += 1

print('Out of {} rolls, {} appeared {} times'.format(rolls, num, ctr))
print('')