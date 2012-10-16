*****
Lists
*****

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
   
