*****
Files
*****

Input and output of strings to a file::

   >>> outfile = open('tmp.txt', 'w')
   # Note: We must output a newline
   >>> outfile.write('This is line #1\n')
   >>> outfile.write('This is line #2\n')
   >>> outfile.write('This is line #3\n')
   >>> outfile.close()
   


Reading an entire file::

   >>> infile = open('tmp.txt', 'r')
   >>> content = infile.read()
   >>> print content
   This is line #1
   This is line #2
   This is line #3
   >>> infile.close()
   

Reading a file one line at a time::

   >>> infile = open('tmp.txt', 'r')
   >>> for line in infile.readlines():
   ...     print 'Line:', line
   ...........................
   Line: This is line #1
   Line: This is line #2
   Line: This is line #3
   >>> infile.close()


``infile.readlines()`` returns a list of lines in the file. For large files use
the file object itself ``infile.xreadlines()``, both of which are iterators for
the lines in the file.


``with`` keyword
================

Files should *always* be closed before the program exits.  When using the basic
``open()`` syntax, it is possible for the programmer to forget to include a
``close()`` call, or for the program to exit with an exception before the file
closes.  Using the ``with`` keyword avoids these pitfalls.  The file is open
only for the block of code indented beneath the ``with`` line - when that code
exits, the file is closed.  This works even if the program exits with an
exception.

::

   >>> with open('/tmp/foobar.txt', 'w') as outfile:
   ...     outfile.write('foo\n')
   ...     outfile.write('bar\n')
   ... 
   >>> print outfile
   <closed file '/tmp/foobar.txt', mode 'w' at 0x7fdb21d8e390>
   >>> with open('/tmp/foobar.txt', 'r') as infile:
   ...     for line in infile:
   ...         print line
   ... 
   foo
   
   bar
   
   >>> 
