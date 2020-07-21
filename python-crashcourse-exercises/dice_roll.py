from random import randint, choice
from math import factorial

class Die:
    def __init__(self, sides=0):
        self.sides = sides


    def roll_die(self):
        rolled_die = randint(1, self.sides)
        print(rolled_die)

die_6 = Die(20)
die_6.roll_die()
