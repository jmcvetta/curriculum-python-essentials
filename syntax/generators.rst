**********
Generators
**********


Functions that yield a result are essentially an iterable::

   def abc():
       yield "a"
       yield "b"
       yield "c"

When we have yield in a function, it implicitly becomes a "generator"
which will act like an iterable::

   >>> abc()
   <generator object abc at 0x7fe30be0a8c0>
   >>> for item in abc():
   ...     print item
   ... 
   a
   b
   c
   
   >>> # We can do it again
   >>> for item in abc():
   ...     print item
   ... 
   a
   b
   c
   >>> # To see what's happening
   >>> l = abc()
   >>> l
   <generator object abc at 0x7fe30be0a910>
   >>> l.next()
   'a'
   >>> l.next()
   'b'
   >>> l.next()
   'c'
   >>> l.next()
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   StopIteration
      
   
# Now let's generate a sequence of unicode characters, equivalent to what we did in the Iterators section::

   # NOTE: Many of these may not be visible characters
   def make_unicode():
       for num in range(50, 1000):
           yield unichr(num)
   
   for letter in make_unicode():
       print letter
