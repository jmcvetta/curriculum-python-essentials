*******
Strings
*******


Strings are immutable, iterable "lists" of characters in Python.
As strings are incredibly important, we will pay a little more
attention to them before moving on to the remaining datatypes.

Basics
======

In python, there is no difference between a single and a double
quoted string...

::

   >>> s1 = 'abc'
   >>> s2 = "abc"
   >>> s1 == s2
   True


Triple quoted, using single or double quotes, is a multiline string.


::

   >>> s = '''this is
   ... a 
   ... multiline
   ... string
   ... '''
   >>> s
   'this is\na \nmultiline\nstring\n'
   >>> print s
   this is
   a 
   multiline
   string
   
   >>> 
   

Raw Strings
-----------

Raw strings are very useful in Regular Expressions.

::

   s4 = r"hello \n world"        # <-- Raw string

Unicode Strings
---------------

In Python 2.x, strings are ASCII.  Starting in Python 3.x, all strings are
unicode by default.

::

   >>> s = u'Hello\u0020World !'
   >>> s
   u'Hello World !'



``string`` module
-----------------


There is also a string module. Most functions in the module are accessible as
instance methods on string types, although there are a few helper attributes
that can't be found elsewhere.

::

   import string
   print string.ascii_letters
   #'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
   print string.digits
   #'0123456789'
   print string.punctuation
   #'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


Operations
----------

Strings can be concatenated with the ``+`` operator::

   >>> word = 'Help' + 'A'
   >>> word
   'HelpA'
   
   
Strings can be repeated with the ``*`` operator::

   >>> '<' + word*5 + '>'
   '<HelpAHelpAHelpAHelpAHelpA>'


Loops
-----

Accessing a string as an iterable in a for loop::

   >>> for ch in s1:
   ...   print ch
   ..............
   a
   b
   c
   d


Index Notation
==============

::

   >>> word = 'HelpA'
   
   >>> word[4]
   'A'
   
   >>> word[0:2]
   'He'
   
   >>> word[2:4]
   'lp'
   
   >>> word[:2]    # The first two characters
   'He'
   
   >>> word[2:]    # Everything except the first two characters
   'lpA'
   
   >>> word[-1]     # The last character
   'A'
   
   >>> word[-0]     # (since -0 equals 0)
   'H'


No reassigning chars::

   >>> word[0] = 'x'
   Traceback (most recent call last):
     File "<stdin>", line 1, in ?
   TypeError: object does not support item assignment

Formatting
==========

Justification::

   >>> "42".rjust(10)
   '        42'
   >>> "42".center(10)
   '    42    '
   >>> "42".ljust(10)
   '42        '

Zero fill padding::

   >>> '12'.zfill(5)
   '00012'
   >>> '-3.14'.zfill(7)
   '-003.14'

Removing extraneous white space::

   >>> '   Get Rid of Whitespace, including newlines   \n'.strip()
   'Get Rid of Whitespace, including newlines'
   >>> '   Get Rid of Whitespace, including newlines   \n'.rstrip()
   '   Get Rid of Whitespace'
   >>> '   Get Rid of Whitespace, including newlines   \n'.lstrip()
   'Get Rid of Whitespace, including newlines   \n'

Various methods::

   >>> "hello, world".split(", ")
   ['hello', 'world']
   
   >>> ", ".join(["hello", "world"])
   'hello, world'
   # Or the same thing, written statically with the string library imported.
   >>> string.join(["hello", "world"], ", ")
   'hello, world'
   
   >>> 'The happy cat ran home.'.upper()
   'THE HAPPY CAT RAN HOME.'
   
   >>> 'The happy cat ran home.'.find('cat')
   10
   
   >>> 'The happy cat ran home.'.find('kitten')
   -1

Modulus (``%``) Operator
------------------------


Python uses the ``%`` (modulus) operator for formatting (modifying) strings.
Within the string to format, a % character marks a token. The ``%s`` is the
conversion type. If we're passing in a string, use "s".

::

   >>> state = 'California'
   >>> 'It never rains in sunny %s.' % state
   'It never rains in sunny California.'

With multiple inputs, we wrap in a tuple::

   >>> "%s %s!" % ("hello", "world")
   'hello world!'

Formatting a floating point output:

* zero filled
* 6 total characters (including decimal)
* precision of 3 (which includes all values, not just post decimal values)

::

   >>> "%06.3g" % 10.5
   '0010.5'

Referencing a value from a named attribute instead of a tuple. Can use a tuple
or a map, not both::

   >>> pets = {'dog': 'Fido', 'cat': 'Claude'}
   >>> 'My dog is named %(dog)s, and my cat %(cat)s.' % pets
   'My dog is named Fido, and my cat Claude.'
   



``.format()`` Method
--------------------

Repeats reference to first argument::

   >>> "First, thou shalt count to {0} then to {0}".format(10, 10)
   'First, thou shalt count to 10 then to 10'


References keyword argument ``food``::

   >>> "I like {food}".format(food='pizza')
   'I like pizza'

Accessing class attributes::

   >>> class Elephant(object):
   ...     weight = 325
   ...     
   ... 
   >>> class Elephant(object):
   ...     weight = 325
   ... 
   >>> e = Elephant()
   >>> "Weight in tons {0.weight}".format(e)      
   'Weight in tons 325'


First element of keyword argument ``players``::

   >>> "Units destroyed: {players[0]}".format(players=[80])
   'Units destroyed: 80'

Referencing items in a dict::

   >>> d = {"dog": "cat"}
   >>> "{0[dog]}".format(d)
   'cat'
   
Or with a more shorthand notation::

   >>> "{dog}".format(**d)
   'cat'


Implicitly references the first positional argument::

   >>> "Bring me a {}".format("shoe") 
   'Bring me a shoe'



New style formatting::

   >>> '{0:<30}'.format('left aligned')
   'left aligned                  '
   >>> '{0:>30}'.format('right aligned')
   '                 right aligned'
   >>> '{0:^30}'.format('centered')
   '           centered           '
   # use '*' as a fill char
   >>> '{0:*^30}'.format('centered')  
   '***********centered***********'
