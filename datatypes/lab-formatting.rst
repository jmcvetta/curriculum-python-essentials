***********************
Lab - String formatting
***********************

Suppose we want to print out a chess or checkerboard using
ASCII characters.

.. literalinclude:: ../labs/formatting.0.py
   :linenos:
   

Solution:

.. literalinclude:: ../labs/formatting.1.py
   :linenos:
   :lines: 15-27
   

Let's try it out:

.. code-block:: console

   $ python formatting.py 
   X X X X 
    X X X X
   X X X X 
    X X X X
   X X X X 
    X X X X
   X X X X 
    X X X X


We can also `visualize the execution`__ of our program with *Python Tutor*.

__ http://www.pythontutor.com/visualize.html#code=def+main()%3A%0A++++dark+%3D+%22X%22%0A++++light+%3D+%22+%22%0A++++for+i+in+range(8)%3A%0A++++++++if+i+%25+2%3A%0A++++++++++++%23+This+is+an+even+row.%0A++++++++++++first+%3D+dark%0A++++++++++++second+%3D+light%0A++++++++else%3A%0A++++++++++++%23+This+is+an+odd+row.%0A++++++++++++first+%3D+light%0A++++++++++++second+%3D+dark%0A++++++++print+%22%7B0%7D%7B1%7D%22.format(first,+second)+*+4%0A%0A%0Aif+__name__+%3D%3D+'__main__'%3A%0A++++main()&mode=display&cumulative=false&py=2&curInstr=0