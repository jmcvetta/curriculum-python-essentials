#!/usr/bin/env python
#
# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.

from dice.dice import Die6
from dice.dice import Die20


def main():
    d6 = Die6()
    d20 = Die20()
    print d6.roll()     # Returns int between 1 and 6
    print d6 + d20      # Returns int between 2 and 26
    print d6 + 15       # Returns int between 16 and 21
    print d6 + "foobar" # Throws exception

if __name__ == '__main__':
    main()
