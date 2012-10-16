#!/usr/bin/env python

'''
Lab - String Formatting

Suppose we want to print out a chess or checkerboard using ASCII characters.

* We need 8 rows and 8 columns.
* We need a character to represent the black squares.
* We need a character to represent the white squares.
* Use the .format() method or the format via % operation.
'''


def main():
    dark = "X"
    light = " "
    for i in range(8):
        if i % 2:
            # This is an even row.
            even = dark
            odd = light
        else:
            # This is an odd row.
            even = light
            odd = dark
        print "{0}{1}".format(odd, even) * 4


if __name__ == '__main__':
    main()