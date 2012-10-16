******
Tuples
******

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
