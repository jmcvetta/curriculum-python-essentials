*******
Classes
*******


Classes are template structures in Python. They are special objects and types
that allow for the creation of unique copies, or instances, of itself. The most
basic type of class is a copy of an empty object.

NOTE: This format is called a "new style class", as it inherits from at least
the Base object type::

   class Employee(object):
       # We use pass because, since we have no content, we need something
       # to tell python that the indentation is correct.
       pass


Inheritence in Python is achieved by passing a comma delimited list of base
classes into a new class. Python classes can exhibit polymorphism and multiple
inheritence.

Bosses are an employee, even though they're the boss::

   class Boss(Employee):
       # Define a class attribute.
       title = "Like a boss."
       def __init__(self, name):
           """Init is the special constructor function, and it is designed
           to be overridden and used by the classes we make.
           
           All class methods in python double as instance methods. They are 
           required to have n+1 arguments, where the first argument is always
           the implicit reference to the instance, usually called self.
           
           When called as a class static method, the caller must pass the
           self reference explicitly, not implicitly.
           """
           # Even though this does nothing, We're going to mimic one way
           # to call a super method in Python.
           super(Boss, self).__init__()
           # Set instance attribute.
           self.name = name
   
   if __name__ == "__main__":
       # Create an empty employee instance.
       peon = Employee()
       # By default, classes are dynamic and we can add attributes to them
       # on the fly (although this can also be turned off with a bit of work).
       peon.name = 'John Peon'
       print "Peon Name:", peon.name
   
       # Create a boss instance.
       boss = Boss("The Boss")
       # Access instance attribute.
       print "Boss Name:", boss.name
       # Instances reference class attributes implicitly.
       print "Boss Title:", boss.title
       
       # Check inheritence
       print isinstance(boss, Boss)
       print isinstance(peon, Boss)
       print issubclass(Boss, Employee)


Getters & Setters
=================

The decorator idea extends to classes. One useful method is when defining public
properties that need to be contrived and don't work well when left as public
properties::

   class Employee(object):
       def __init__(self, fname, lname):
           self.fname = fname
           self.lname = lname
       @property
       def name(self):
           """A full name, contrived from two other properties."""
           return self.fname + " " + self.lname
       # If we define the property, we can also define a setter and a
       # deleter, in our example they would be called:
       # @x.setter
       # @x.deleter
       # If we don't define them, the property is not settable
       # and is not deletable.
       
   
   if __name__ == "__main__":
       e = Employee("like", "a boss")
       # There are no private properties in Python
       print e.fname, e.lname
       # But there are contrived properties
       print e.name
       # The following will be an error since the public interface
       # is not callable.
       #print e.name()
       # The following will also be an error since we didn't define
       # a setter.
       #e.name = "hola"


.. todo:: Rewrite text for this section for better clarity.

