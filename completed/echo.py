"""
Mini lab.

Write a small bit of code that:

* Queries the user for input.
* If the input is a number, tell the user that they gave us
  a number, and output the number.
* If the input is not a number, tell repeate the string that
  the user gave us.
* If the user input is the word "quit", after doing the above,
  quit the while loop and the program.
"""

def speak(m):
    print "Echo:", m

while True:
    try:
        s = raw_input("What would you like me to echo? ")
        num = int(s)
    except ValueError:
        # Input was not a number, echo it back.
        speak(s)
    else:
        # Input was a number, things didn't throw.
        print "You gave me a number!"
        speak(num)
    finally:
        # Quit if the user types in "quit"
        if s == "quit":
            print "quitting."
            break
