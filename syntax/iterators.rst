*********
Iterators
*********


An iterator allows you to loop over a set of data generated one value at a time.
Using an iterator is more memory efficient than storing the entire sequence in
memory and iterating over that.

Example::

   # An iterable returns an iterator object that can be processed in a for loop
   class Unicoder():
       # The sole purpose of this class is to build an iterator for
       # testing.
       current = None
       start = 50
       stop = 1000
       def __iter__(self):
           self.current = self.start
           return self
       def next(self):
           if self.current <= self.stop:
               ret = unichr(self.current)
               self.current += 1
               return ret
           else:
               # This step is important.
               # We are _required_ to raise StopIteration in an iterator.
               raise StopIteration()
   
   u = Unicoder()
   for char in u:
       print char
   
