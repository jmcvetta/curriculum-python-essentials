****
Math
****

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
