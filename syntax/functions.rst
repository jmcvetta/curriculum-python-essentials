*********
Functions
*********

::

   def fib(n):    # write Fibonacci series up to n
   	"""Print a Fibonacci series up to n."""
   	a, b = 0, 1
   	while a < n:
   		print a,
   		a, b = b, a+b

Now call the function we just defined in various ways::

   fib(2000)


Print the funtion object::

   print fib


Reference the function and call::

   f = fib
   f(100)


It's usually better to have a function return a value. Rewrite our funtion above
so it's like what follows::


   def fib(n):
   	"""Return a list of the Fibonacci series up to n."""
   	a, b = 0, 1
   	results = []
   	while a < n:
   		results.append(a)
   		a, b = b, a+b
   	return results

Run it::

   print fib(1000)


Calling the function above without any variables will throw an error::

   fib()
   # You'll get a traceback.

But every formal parameter to a function can be given a default value. Rewrite
the above as follows (just changing the param)::

   def fib(n=100):
   	"""Return a list of the Fibonacci series up to n, default
   	to 100."""
   	a, b = 0, 1
   	results = []
   	while a < n:
   		results.append(a)
   		a, b = b, a+b
   	return results

Now there is no more error::

   print fib()


We can also specifically label an argument::

   print fib(n=1000)



Functions can also take a variable number of unlabeled arguments that, if passed
in, will be captured in a list::

   def echo(*words):
   	print "You passed in {0} words.".format(len(words))
   	for word in words:
   		print "A word: ", word
   
Call the function::

   echo()
   echo("hello", "world")


Functions can also take a variable number of labeled arguments that, if passed
in, will be captured in a dictionary::

   def echo2(**words):
   	print "You passed in {0} key:value pairs.".format(len(words))
   	for k, v in words.items():
   		print k, v 
		
Call the function, making sure to label the arguments::

   echo2(hello="world", the="universe")

It is possible to combine formal arguments with both the unlabeled variable
arguments and the labeled variable arguments. When defining a function, formal
arguments must come first, followed by unlabeled variable arguments, followed
finally by labeled variable arguments.
