********
Integers
********

Numbers are immutable.

``int``
=======

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
====

* Unlimited precision [#f1]_

* Denoted by 'l' or 'L', no difference in case

* **Note:** This is disappearing in Python 3.x.  ''int'' and longs operate the
  same in Python 3.x. In other words the max int is essentially boundless.
  

.. todo::


::

   >>> 42l == 42
   True
   >>> type(42L)
   >>> type(42L) == type(42)
   False

.. rubric:: Footnotes

.. [#f1] http://docs.python.org/library/stdtypes.html#numeric-types-int-float-long-complex