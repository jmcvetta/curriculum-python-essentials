#!/usr/bin/env python
#
# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.

import unittest
from random import randint
from die import Die

class DieTest(unittest.TestCase):

    def setUp(self):
        pass # do some setup stuff

    def testInit(self):
        self.assertRaises(ValueError, Die, 0)


    def testRoll(self):
        pass

    def testAdd(self):
        pass


if __name__ == '__main__':
    unittest.main()
