*******
Decimal
*******

Not a built in type, but this module is useful for people who need reliable
precision with the floating points they use.

We need to import the decimal module:

::

   import decimal
   

We'll import the Decimal class by itself for easier use.

::

   from decimal import Decimal


Now we can use the Decimal type, which defaults to a precision level of 28
digits.

::

   >>> Decimal("1") / Decimal("7")
   Decimal('0.1428571428571428571428571429')


Helps with traditionally tricky, and unreliable, floating point arithmetic.

Note: Here we pass in strings, not floating point numbers. If we pass floating
point numbers in, we'll get exact addition from our inexact binary floating
point numbers: garbage in, garbage out.

::

   >>> 10 + 0.000000000000000001
   10.0
   >>> Decimal("10") + Decimal("0.000000000000000001")
   Decimal('10.000000000000000001')


Get the current precision of a decimal, and other settings for the module:

::

   >>> decimal.getcontext()
   Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999999, Emax=999999999, capitals=1, flags=[Inexact, Rounded], traps=[InvalidOperation, Overflow, DivisionByZero])
