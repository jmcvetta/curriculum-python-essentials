****
Sets
****

A set is an unordered collection with no duplicate elements

::

   >>> basket = ['apple', 'orange', 'apple', 'pear']
   >>> fruit = set(basket)               
   >>> fruit
   set(['orange', 'pear', 'apple'])
   
   >>> 'orange' in fruit
   True
   >>> 'crabgrass' in fruit
   False


Set Operators
=============

::

   >>> a = set('xyzzy')
   >>> b = set('xxy')
   >>> a
   set(['y', 'x', 'z'])
   >>> b
   set(['y', 'x'])
   
   >>> # letters in a but not in b
   >>> a - b                              
   set(['z'])
   
   >>> # letters in either a or b
   >>> a | b                              
   set(['y', 'x', 'z'])
   
   >>> # letters in both a and b
   >>> a & b                              
   set(['y', 'x'])
   
   >>> # letters in a or b but not both
   >>> a ^ b                              
   set(['z'])
   
   >>> # And a failed operation
   >>> a + b
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: unsupported operand type(s) for +: 'set' and 'set'
   
   
