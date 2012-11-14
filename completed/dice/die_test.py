#!/usr/bin/env python
#
# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.

import unittest
from random import randint
from die import Die

class DieTest(unittest.TestCase):

    def setUp(self):
        # do some setup stuff
        pass

    def testInit(self):
        #
        # Initialize valid die
        #
        d0, sides = self.newDie()
        self.assertEqual(d0.sides, sides)
        #
        # Initialize die with invalid number of sides
        #
        self.assertRaises(ValueError, Die, 0)
        self.assertRaises(ValueError, Die, -15)
        self.assertRaises(ValueError, Die, 2.5)
        self.assertRaises(ValueError, Die, 'asparagus')
        self.assertRaises(ValueError, Die, Die)
        self.assertRaises(TypeError, Die) # No arg to constructor

    def newDie(self):
        sides = randint(2, 999999999)
        d0 = Die(sides=sides)
        return d0, sides

    def testRoll(self):
        for i in range(1000):
            d0, sides = self.newDie()
            roll_value = d0.roll()
            expr = sides >= roll_value >= 1
            msg =  'Expected value between 1 and %s from roll, but got %s' % (sides, roll_value)
            self.assertTrue(expr, msg)

    def testAdd(self):
        for i in range(1000):
            #
            # Add two dice
            #
            d0, sides0 = self.newDie()
            d1, sides1 = self.newDie()
            min_roll = 2
            max_roll = sides0 + sides1
            this_roll = d0 + d1
            expr = max_roll >= this_roll >= min_roll
            msg =  'Expected value between %s and %s from roll,' % (min_roll, max_roll)
            msg += 'but got %s' % this_roll
            self.assertTrue(expr, msg)
            #
            # Add die to integer
            #
            an_integer = randint(1, 999999999)
            max_roll = sides0 + an_integer
            this_roll = d0 + an_integer
            expr = max_roll >= this_roll >= min_roll
            msg =  'Expected value between %s and %s from roll,' % (min_roll, max_roll)
            msg += 'but got %s' % this_roll
            self.assertTrue(expr, msg)
        #
        # Add die to invalid types
        #
        with self.assertRaises(ValueError):
            d0 + "foobar"
        with self.assertRaises(ValueError):
            d0 + 2.5
        with self.assertRaises(ValueError):
            d0 + Die



if __name__ == '__main__':
    unittest.main()
