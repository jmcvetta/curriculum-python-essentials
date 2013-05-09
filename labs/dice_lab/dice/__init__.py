# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.

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
* If a die is added to something other than an integer or another die, the
  operation should fail with an exception.
'''

VERSION = '0.1'