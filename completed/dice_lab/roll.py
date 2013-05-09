#!/usr/bin/env python
#
# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.

from dice.dice import Die6
from dice.dice import Die20


def main():
    d6 = Die6()
    d20 = Die20()
    print d6.roll()
    print d6 + d20
    print d6 + "foobar"

if __name__ == '__main__':
    main()
