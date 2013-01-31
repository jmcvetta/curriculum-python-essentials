***********
Collections
***********


Lists
=====

Lists are mutable, dynamic arrays. 

They are arrays in the sense that you can index items in a list  (for example
``mylist[3]``) and you can select sub-ranges (for example ``mylist[2:4]``). They
are dynamic in the sense that you can add and remove items after the list is
created.


# To create a list use:

::

   >>> items = [111, 222, 333]
   >>> items
   [111, 222, 333]
   >>> len(items)
   3
   >>> items[0]
   111
   >>> items[3]
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   IndexError: list index out of range


   >>> list(1, 2, 3)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: list() takes at most 1 argument (3 given)
   >>> list("123")
   ['1', '2', '3']
   >>> list([1, 2, 3])
   [1, 2, 3]
   >>> list((1, 2, 3))
   [1, 2, 3]



To add an item to the end of a list, use:

::

   >>> items.append(444)
   >>> items
   [111, 222, 333, 444]



To insert an item into a list, use: 

::

   >>> items.insert(0, -1)
   >>> items
   [-1, 111, 222, 333, 444]



Pop from the right

::

   >>> items.pop()
   444
   >>> items
   [-1, 111, 222, 333]


Iterate over items in the list

::

   >>> for item in items:
   ...   print 'item:', item
   ...
   item: -1
   item: 111
   item: 222
   item: 333

Other list operations

::

   >>> items.count(111)
   1
   >>> items.index(-1)
   0
   >>> items.remove(-1)
   >>> items
   [111, 222, 333]
   >>> items.append(111)
   >>> items.remove(111)
   >>> items
   [222, 333, 111]
   >>> items.reverse()
   >>> items
   [111, 333, 222]
   >>> items.sort()
   >>> items
   [111, 222, 333]


Check if an item is in the list

::

   >>> 111 in items
   True

Remove an item at a particular index

::

   >>> del items[1]
   [111, 333]


Concatenation comparison

::

   >>> ['a'] + ['b']
   ['a', 'b']
   >>> 'a' + 'b'
   'ab'


Tuples
======

Tuples are essentially immutable lists.

Helpful when you want to preserve and protect the data, but have the output
flexibility of a list.

::

   >>> t = 12345, 54321, 'hello!'
   >>> t[0]
   12345

   >>> t
   (12345, 54321, 'hello!')


Tuples may be nested:

::

   >>> u = t, (1, 2, 3, 4, 5)

   >>> u
   ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))



Tuple packing

::

   >>> t = 12345, 54321,  'hello!'
   >>> t
   (12345, 54321, 'hello!')
   >>> x, y, z = t
   >>> x
   12345
   >>> y
   54321
   >>> z
   'hello!'



Be careful, it is easy to confuse a logical expression and a single-item tuple.

::

   >>> astring = ('hello')
   >>> astring
   'hello'
   # Length of the string, not a tuple
   >>> len(astring)
   5



Note the trailing comma

::

   >>> a = ('hello',) 
   ('hello',)
   >>> len(a)
   1
   # convert list to tuple
   >>> a = tuple(['hello'])
   >>> a
   ('hello',)



Sequence packing

::

   >>> atuple = 'hello', 'world' 
   >>> atuple
   # Sequencce unpacking
   >>> h, w = atuple 
   >>> h
   'hello'
   >>> w
   'world'


Dictionaries
============


Dictionaries are associative arrays.

Keys are hashable types, like strings and numbers.  Tuples can also be keys, as
long as they contain only strings, numbers, and more tuples.

::

   >>> tel = {'jack': 4098, 'sape': 4139}
   >>> tel['guido'] = 4127
   >>> tel
   {'sape': 4139, 'guido': 4127, 'jack': 4098}
   
   >>> tel['jack']
   4098
   >>> len(tel)
   2
   >>> type(tel)
   <type 'dict'>
   
   >>> del tel['sape']
   >>> tel['irv'] = 4127
   >>> tel
   {'guido': 4127, 'irv': 4127, 'jack': 4098}

   >>> tel.keys()
   ['guido', 'irv', 'jack']
   >>> tel.values()
   [4098, 4127, 4127]
   >>> tel.items()
   [('jack', 4098), ('irv', 4127), ('guido', 4127)]
   >>> type(tel.items())
   <type 'list'>
   >>> type(tel.items()[0])
   <type 'tuple'>
   
   >>> 'guido' in tel
   True
   >>> 42 not in tel
   True

Shallow copy

::

   >>> hello = tel.copy()
   >>> hello
   {'guido': 4127, 'irv': 4127, 'jack': 4098}


Conversion to a dictionary

::

   >>> dict(sape=4139, guido=4127, jack=4098)
   {'sape': 4139, 'jack': 4098, 'guido': 4127}


Retrieving key and value in dictionaries

::

   >>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
   >>> for k, v in knights.iteritems():
   ...     print k, v
   ..................
   gallahad the pure
   robin the brave


Sets
====

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
-------------

::

	>>> a = set('xyzzyqtt')
	>>> b = set('zzytrr')
	>>> a
	set(['y', 'x', 'z', 'q', 't'])
	>>> b
	set(['y', 'r', 'z', 't'])
	>>> # letters in a but not in b
	
	>>> a - b
	set(['q', 'x'])
	>>> # letters in either a or b
	
	>>> a | b
	set(['q', 'r', 't', 'y', 'x', 'z'])
	>>> # letters in both a and b
	
	>>> a & b
	set(['y', 'z', 't'])
	>>> # letters in a or b but not both
	
	>>> a ^ b
	set(['q', 'x', 'r'])
	>>> # And a failed operation
	
	>>> a + b
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: unsupported operand type(s) for +: 'set' and 'set'
	


.. todo::

   Add another character to the set math examples, to better illustrate diff
   between - and ^ operators.




