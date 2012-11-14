#!/usr/bin/env python
'''
Lab - Dice

Make a package of dice rolling utilities.
* Make a simple Die class for the basic rolling of a die
* Make D6 (six-sided) and D20 (twenty-sided) subclasses
* Each Die instance will have a roll() method, returning a random
  number between 1 and the number of sides on that die.
* When one die instance is added to another die instance, roll() is
  called on both instances and the results added together.
* When a die instance is added to an integer, the instance's roll()
  method is called, and the result is added to the integer.
'''

from random import randint

class Die(object):
    '''A single die'''

    def __init__(self, sides):
        if not type(sides) == int:
            msg = "Argument 'sides' must be an int, but you supplied %s" % type(sides)
            raise ValueError(msg)
        if not sides >= 2:
            msg = "Die must have at least 2 dies, but you gave %s" % sides
            raise ValueError(msg)
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)

    def __add__(self, other):
        if isinstance(other, Die):
            return self.roll() + other.roll()
        elif isinstance(other, int):
            return self.roll() + other
        else:
            msg =  'Can only add die instance to another die '
            msg += 'or an integer; but you tried a %s' % type(other)
            raise ValueError(msg)



def main():
    d12 = Die(sides=12)
    d50 = Die(sides=50)
    print d12 + d50
    print d12 + 14

if __name__ == '__main__':
    main()
