*********
Operators
*********

Some different forms of operators in Python, to go with the usual C operators
everyone is likely familiar with.

The and and or operators do not return a boolean value, instead they return a
value that will result in a truthy pass or a falsey fail, and are safe to use
anywhere a normal logic check would be used::

   >>> 1 and 2
   2
   >>> 1 or 2
   1
   >>> "" or 0
   0



Normal logic checks::

   >>> bool("" or 0)
   False
   >>> 1 == 2
   False
   >>> 1 != 2
   True
   >>> 1 is 2
   False
   >>> 1 is not 2
   True
   


In Python 3.x, integer division that should return a fraction will return a
float.

In Python 2.x, it doesn't::

   >>> 1 / 2
   0
   # Results rounded toward minus infinity.
   >>> -1 / 2
   -1
   # Floored operation on quotient, more useful in Python 3.x
   # when you don't want a float returned.
   >>> -1 // 2
   -1
   # Easy way to get (quotient, remainder)
   >>> divmod(1, 2)
   (0, 1)



Powers, both valid ways of doing things::

   >>> 2 ** 8
   256
   >>> pow(2, 8)
   256
   


Python does not have a post- or prefix incrementor or decrementor::

   >>> a = 1
   >>> a++
     File "<stdin>", line 1
       a++
         ^
   SyntaxError: invalid syntax
   # The proper way to increment or decrement in python is
   >>> a += 1
   >>> a
   2
