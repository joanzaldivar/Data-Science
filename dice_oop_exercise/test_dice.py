# Tests for the dice.py file

from unittest import TestCase
from dice import Die


class TestDie(TestCase):

    def test_expected(self):
        d = Die()
        self.assertEqual(3.5, d.expected(), "The expected value of a 6 sided die should be 3.5")  # d.expected()   >>>    Die.expected(d)

    def test_add(self):
        d1 = Die(num_sides=6)
        d2 = Die(num_sides=8)
        sum_expected = d1 + d2  # >>>   d1.__add__(d2)  >>> Die.__add__(d1, d2)
        self.assertEqual(8, sum_expected, "The sum of a 6 sided die and an 8 sided die should be the sum of their expected values, which is 8")
