#!/usr/bin/env python
#-------------------------------------------------------------------------------
# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.
#-------------------------------------------------------------------------------

'''
Lab - String Formatting

Suppose we want to print out a checker board using ASCII characters.

* We need 8 rows and 8 columns.
* We need a character to represent the black squares.
* We need a character to represent the white squares.
* Use the .format() method or format with the % operator.
'''

DARK = "X"
LIGHT = " "

def main():
    for i in range(8):
        if i % 2:
            # This is an even row.
            first = DARK
            second = LIGHT
        else:
            # This is an odd row.
            first = LIGHT
            second = DARK
        print "{0}{1}".format(first, second) * 4


if __name__ == '__main__':
    main()