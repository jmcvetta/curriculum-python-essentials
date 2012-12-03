#!/usr/bin/env python
#-------------------------------------------------------------------------------
# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.
#-------------------------------------------------------------------------------
'''
Lab - Echo

Write a program that:

* Queries the user for input.
* If the input is an integer, tell the user that they gave us
  an integer, and echo the input.
* If the input is not a number, echo the input.
* If the user input is the word "quit", after doing the above,
  exit the program.
* Repeat until the user quits
'''

def speak(m):
    print "Echo:", m

def main():
    while True:
        try:
            s = raw_input("What sayest thou?")
            num = int(s)
        except ValueError:
            # Input was not a number, echo it back.
            print 'Echo: %s' % s
        else:
            # Input was a number, things didn't throw.
            print "You typed an integer!"
            print 'Echo: %s' % s
        finally:
            # Quit if the user types in "quit"
            if s.lower() in ['quit', 'exit', 'q']:
                print "Quitting."
                break

if __name__ == '__main__':
    main()