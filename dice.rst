**********
Lab - Dice
**********

Let's suppose we want to make a set of dice rolling utilities.  We will define a
generic ``Die`` class, representing a single die with an arbitrary number of
sides.  We will also define six-sided ``Die6`` and twenty-sided ``Die20`` subclasses.

Pseudorandom Number Generator
=============================

We will use the ``randint`` function from the ``random`` library to generate
pseudo-random numbers for our dice rolls.  It takes two integers as arguments, a
min and max, and returns a random integer between the two.

**Note:** Do NOT use Python's standard ``random`` library for
cryptographic purposes - it is deterministic and NOT a cryptographically secure
PRNG.

File Layout
===========

We will start with a file layout like this::

   dice_lab/
      roll.py
      dice/
         __init__.py
         die.py
         dice.py


Code Stubs
==========

roll.py
-------

This script contains an example of using the classes.  If you can run the
example, your dice classes are at least minimally working.

.. literalinclude:: labs/dice_lab/roll.py
   :lines: 5-

dice/__init__.py
----------------

The ``__init__.py`` file will be mostly empty, containing only a docstring and a
``VERSION`` variable:

.. literalinclude:: labs/dice_lab/dice/__init__.py
   :lines: 3-

dice/die.py
-----------

The main ``Die`` class is found in ``die.py``:

.. literalinclude:: labs/dice_lab/dice/die.py
   :lines: 4-

dice/dice.py
------------

Two subclasses, representing six- and twenty-sided dice, are found in
``dice.py``.  

.. literalinclude:: labs/dice_lab/dice/dice.py
   :linenos:
   :lines: 6-


