********
Packages
********

So far we have been working with fairly short, simple programs contained in
single files.  That style works great for scripts; but most real applications
are more complex, and thus better split among several files.

Package Layout
==============

Consider the file layout of a sample program::

  foobar/
      __init__.py
      foo.py
      bar/
          __init__.py
          baz.py




``__init__.py``
===============

Python considers any folder that is on the ``PYTHONPATH`` and contains an
``__init__.py`` file to be a package, and thus importable.

The ``__init__.py`` file's primary purpose is to be a marker - any folder
containing an ``__init__.py`` file is an importable package.  The file likewise
defines the top level of said package's namespace.  

Almost *every* Python package contains an ``__init__.py`` file; and the file
name tells us *nothing* about the contents of the file, except that it is
package marker.  Therefore it is considered inappropriate to put real
functionality - class definitions, functions, etc - into an ``__init__.py``
file.

It is commonplace for ``__init__.py`` to be left completely empty.  If it does
contain code, it will typically be limited to docstrings, version constants, and
import statements.  Since the ``__init__.py`` file is the top level of it's
package's namespace, by importing an object into ``__init__.py`` we promote that
into the module's top level namespace.  

Consider what an ``__init__.py`` file from the example program above might look
like::

   '''
   Foobar
   
   A program that puts the foo into bar!  (Caution, use at your own risk.  Your
   mileage may vary.)
   '''
   
   VERSION = '0.1'
   
   from foo import Spam
   from bar.baz import Eggs


Importing Packages
==================

In this example, two classes will be available in the top level namespace of the
package:  ``Spam``, which is defined in ``foobar/foo.py``; and ``Eggs`` which is
defined in ``foobar/bar/baz.py``.  Both classes were imported above into
``__init__.py``. Consequently code outside this package can import those classes
like so::

   from foobar import VERSION
   from foobar import Spam
   from foobar import Eggs
   # Not imported in __init__.py, so we have to use the full path:
   from foobar.bar.baz import Ham


Note that in Python, unlike in Java, it is commonplace for multiple class
definitions to live in one file. Nor is there necessarily any relationship
between the name of a file and the name(s) of the object(s) it contains.
