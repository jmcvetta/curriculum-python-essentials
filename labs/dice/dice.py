# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.

from die import Die


class Die6(Die):
    '''
    A six-sided die
    '''
    pass


class Die20(Die):
    '''
    A twenty-sided die
    '''
    pass


def main():
    d6 = Die6()
    d20 = Die20()
    print d6.roll()
    print d6 + d20
    print d6 + 14