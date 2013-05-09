# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.

from random import randint

class Die(object):
    '''A single die with arbitrarily many sides.'''
    
    def roll(self):
        '''Returns a random number between 1 and the number of sides on this die'''
        pass
    
    def __add__(self, other):
        '''Adds the result of rolling this die to an integer, or to the result of rolling 
        another die.'''
        pass

