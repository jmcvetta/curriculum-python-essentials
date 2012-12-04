*****
Scope
*****

Scope chain is functional in Python::

   # Global
   x = 5
   # Function local
   def h():
       x = 3
       def q():
           x = 9
           # local q(), should print 9
           print x
       q()
       # local to h(), should print 3
       print x
   
   # Run h
   h()
   # Global x, should print 5
   print x


This will reference the global since no local x is defined::

   x = 5
   def f():
       print x
   
This will reference, *and* change the global::
   
   x = 5
   def f():
       global x
       x = 3
       print x
   
   # After running the above function, do the following
   print x
