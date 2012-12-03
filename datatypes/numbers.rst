*******
Numbers
*******


Integers
========

Numbers are immutable.

``int``
-------

``int`` is fixed precision, at least 32 bits.

::

   >>> width = 20
   >>> height = 5*9
   >>> width * height
   900

   >>> type(900)
   >>> type(42) == type(900)
   True
   
   >>> int("42")
   >>> int('42')
   >>> int("""42""")
   >>> int("42abc")
   >>> int("abc")
   >>> int("100", 2)


Long
----

* Unlimited precision [#f1]_

* Denoted by 'l' or 'L', no difference in case

* **Note:** This is disappearing in Python 3.x.  ''int'' and longs operate the
  same in Python 3.x. In other words the max int is essentially boundless.
  

::

   >>> 42l == 42
   True
   >>> type(42L)
   >>> type(42L) == type(42)
   False


Floating Point Numbers
======================

Float, system dependent precision:

::

   >>> 3 * 3.75 / 1.5
   7.5

   >>> type(4.2)
   >>> type(42) == type(42.0)
   False
   
   >>> float("42")
   >>> float(42)
   >>> int(42.0)


Float allows us to get access to a special infinity value.

::

   >>> i = float("inf")
   >>> type(i)
   >>> 1000000000000 < i
   True


Most types and objects, even primitive ones, have object methods and properties.

Need to wrap floating points for this to work.

::

   >>> (3.2).is_integer()
   False
   >>> (3.0).is_integer()
   True


Complex Numbers
===============

Complex, an example of a type that has a unique creation syntax and object
oriented property access. Most people probably won't use complex, but it's a
good intro to the subtleties of Python types and built in language mechanics.

::

   >>> a = 1.5+0.5j
   >>> a.real
   1.5
   >>> a.imag
   0.5
   >>> b = 1.4+0.3j
   >>> a + b
   (2.9+0.8j)
   

Math
====

Modulus::

   >>> 8.0 / 3.0
   2.6666666666666665
   >>> 8.0 % 3.0
   2.0
   >>> 8 % 3
   2
   >>> 9.0 / 3.0
   3.0
   >>> 9 % 3
   0


Basic math functions::

   >>> round(42.01)
   42
   >>> round(42.01, 2)
   42.009999999999998
   >>> abs(-42)
   42
   >>> divmod(42, 2)
   (21, 0)
   >>> pow(2, 8)
   256


Many utility functions are available from the ``math`` library::

   >>> import math
   >>> math.trunc(42.0)
   42
   >>> math.floor(42.9999)
   42.0
   >>> math.ceil(42.0001)
   43.0
   >>> math.trunc(math.ceil(42.0001))
   43
   >>> math.pi
   3.1415926535897931
   >>> math.degrees(2*math.pi)
   360.0


Decimal Class
=============

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





.. rubric:: Footnotes

.. [#f1] http://docs.python.org/library/stdtypes.html#numeric-types-int-float-long-complex