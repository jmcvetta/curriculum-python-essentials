*****
Loops
*****

for
===

::

   >>> l = [111, 222, 333, 444]
   >>> for item in l:
   ...     print item
   ... 
   111
   222
   333
   444
   

while
=====

Fibonacci series::

   >>> a, b = 0, 1
   >>> while b < 10:
   ...     print b
   ...     a, b = b, a+b
   ... 
   1
   1
   2
   3
   5
   8
   


Using Range::

   >>> range(10)
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



Other range uses::

   >>> range(5, 10)
   [5, 6, 7, 8, 9]
   >>> range(0, 10, 3)
   [0, 3, 6, 9]



Enumerate::

   >>> for i, v in enumerate(['tic', 'tac', 'toe']):
   ...     print i, v
   ..................
   0 tic
   1 tac
   2 toe
   


Dictionaries::

   >>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
   >>> for k, v in knights.iteritems():
   ...     print k, v
   ..................
   gallahad the pure
   robin the brave
