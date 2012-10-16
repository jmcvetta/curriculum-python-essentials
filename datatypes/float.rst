**********************
Floating Point Numbers
**********************

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
