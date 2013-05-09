# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.

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

#    def __add__(self, other):
#        if isinstance(other, Die):
#            return self.roll() + other.roll()
#        elif isinstance(other, int):
#            return self.roll() + other
#        else:
#            msg =  'Can only add die instance to another die '
#            msg += 'or an integer; but you tried a %s' % type(other)
#            raise ValueError(msg)
    
    def __add__(self, other):
        return other + self.roll()
