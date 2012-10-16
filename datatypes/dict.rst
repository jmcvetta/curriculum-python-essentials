************
Dictionaries
************


Dictionaries are assotiative arrays.

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
