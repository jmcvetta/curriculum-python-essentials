**********
Lab - Dice
**********

Let's suppose we want to make a set of dice rolling utilities.  We will define a
generic ``Die`` class, representing a single die with an arbitrary number of
sides.  We will also define six-sided ``Die6`` and twenty-sided ``Die20`` subclasses.


Multi-file Packages
===================

So far we have been working with fairly short, simple programs contained in
single files.  That style works great for scripts; but most real applications
are more complex, and thus better split among several files.


Declaring a Package
-------------------

Python considers any folder that is on the ``PYTHONPATH`` and contains an
``__init__.py`` file to be a package, and thus importable.

The ``__init__.py`` file's primary purpose is to be a marker - any folder
containing an ``__init__.py`` file is an importable package.  The file likewise
defines the top level of said package's namespace.  

Almost *every* Python package contains an ``__init__.py`` file; and  the file
name tells us *nothing* about the contents of the file, except that it is
package marker.  Therefore it is considered inappropriate to put real
functionality - class definitions, functions, etc - into an ``__init__.py``
file.
