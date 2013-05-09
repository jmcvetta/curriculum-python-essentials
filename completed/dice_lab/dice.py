#!/usr/bin/env python
#
# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.

from die import Die

class Die6(Die):
    '''A six-sided die'''

    def __init__(self):
        super(Die6, self).__init__(sides=6)

class Die20(Die):
    '''A twenty-sided die'''

    def __init__(self):
        super(Die20, self).__init__(sides=20)



def main():
    d6 = Die6()
    d20 = Die20()
    print d6.roll()
    print d6 + d20
    print d6 + "foobar"

if __name__ == '__main__':
    main()
