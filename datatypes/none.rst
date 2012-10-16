*********
None Type
*********

``None`` is Python's null type.

None behaves like one would expact, and it can reliably be tested for, even
against things like False and 0.

::

   >>> type(None)
   <type 'NoneType'>
   
   >>> None == ""
   False
   
   >>> None == 0
   False
   
   >>> None == False
   False
   
   >>> None == None
   True
  
