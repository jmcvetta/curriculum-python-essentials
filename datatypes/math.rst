****
Math
****


Basic math functions

::

   >>> round(42.01)
   42


Likely will cause a precision problem

::

   >>> round(42.01, 2)
   42.009999999999998
   >>> abs(-42)
   42
   >>> divmod(42, 2)
   (21, 0)
   >>> pow(2, 8)
   256


Basic math object

::

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
