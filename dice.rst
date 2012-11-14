**********
Lab - Dice
**********

Let's suppose we want to make a set of dice rolling utilities.  We will define a
generic ``Die`` class, representing a single die with an arbitrary number of
sides.  We will also define six-sided ``Die6`` and twenty-sided ``Die20`` subclasses.

We will start with a file layout like this::

   dice/
      __init__.py
      die.py
      dice.py
      

The ``__init__.py`` file will be mostly empty, containing only a docstring, a
``VERSION`` variable, and a few import statements:

.. literalinclude:: labs/dice/__init__.py
   :linenos:
   :lines: 4-

The main die class is found in ``die.py``:

.. literalinclude:: labs/dice/die.py
   :linenos:
   :lines: 4-



.. if config:: instructor == True

   We define several common subclasses for convenience in ``dice.py``:

   .. literalinclude:: labs/dice/dice.py
      :linenos:
      :lines: 4-