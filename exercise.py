
Exercise 1 - Python.ipynb_
Introduction to Python programming

This entire notebook is purely due to the efforts of J.R. Johansson (http://jrjohansson.github.io.). Hats off, sir
Python program files

    Python code is usually stored in text files with the file ending ".py":

    myprogram.py

    Every line in a Python program file is assumed to be a Python statement, or part thereof.
        The only exception is comment lines, which start with the character # (optionally preceded by an arbitrary number of white-space characters, i.e., tabs or spaces). Comment lines are usually ignored by the Python interpreter.

    To run our Python program from the command line we use:

    $ python myprogram.py

    On UNIX systems it is common to define the path to the interpreter on the first line of the program (note that this is a comment line as far as the Python interpreter is concerned):

    # !/usr/bin/env python

    If we do, and if we additionally set the file script to be executable, we can run the program like this:

    $ myprogram.py

IPython notebooks (a.k.a Jupyter Notebooks)

This file - an IPython notebook - does not follow the standard pattern with Python code in a text file. Instead, an IPython notebook is stored as a file in the JSON format. The advantage is that we can mix formatted text, Python code and code output. It requires the IPython notebook server to run it though, and therefore isn't a stand-alone Python program as described above. Other than that, there is no difference between the Python code that goes into a program file or an IPython notebook.
Modules

Most of the functionality in Python is provided by modules. The Python Standard Library is a large collection of modules that provides cross-platform implementations of common facilities such as access to the operating system, file I/O, string management, network communication, and much more.
References

    The Python Language Reference: http://docs.python.org/2/reference/index.html
    The Python Standard Library: http://docs.python.org/2/library/

To use a module in a Python program it first has to be imported. A module can be imported using the import statement. For example, to import the module math, which contains many standard mathematical functions, we can do:
[ ]

import math

This includes the whole module and makes it available for use later in the program. For example, we can do:
[ ]

import math

​

x = math.cos(2 * math.pi)

​

print(x)

Alternatively, we can chose to import all symbols (functions and variables) in a module to the current namespace (so that we don't need to use the prefix "math." every time we use something from the math module:
[ ]

from math import *

​

x = cos(2 * pi)

​

print(x)

This pattern can be very convenient, but in large programs that include many modules it is often a good idea to keep the symbols from each module in their own namespaces, by using the import math pattern. This would elminate potentially confusing problems with name space collisions.

As a third alternative, we can chose to import only a few selected symbols from a module by explicitly listing which ones we want to import instead of using the wildcard character *:
[ ]

from math import cos, pi

​

x = cos(2 * pi)

​

print(x)

Looking at what a module contains, and its documentation
↳ 7 cells hidden
Variables and types
↳ 34 cells hidden
Operators and comparisons
↳ 16 cells hidden
Compound types: Strings, List and dictionaries
↳ 69 cells hidden
Control Flow
Conditional statements: if, elif, else

The Python syntax for conditional execution of code uses the keywords if, elif (else if), else:
[ ]

statement1 = False

statement2 = False

​

if statement1:

    print("statement1 is True")

    

elif statement2:

    print("statement2 is True")

    

else:

    print("statement1 and statement2 are False")

For the first time, here we encounted a peculiar and unusual aspect of the Python programming language: Program blocks are defined by their indentation level.

Compare to the equivalent C code:

if (statement1)
{
    printf("statement1 is True\n");
}
else if (statement2)
{
    printf("statement2 is True\n");
}
else
{
    printf("statement1 and statement2 are False\n");
}

In C blocks are defined by the enclosing curly brakets { and }. And the level of indentation (white space before the code statements) does not matter (completely optional).

But in Python, the extent of a code block is defined by the indentation level (usually a tab or say four white spaces). This means that we have to be careful to indent our code correctly, or else we will get syntax errors.
Examples:
[ ]

statement1 = statement2 = True

​

if statement1:

    if statement2:

        print("both statement1 and statement2 are True")

[ ]

# Bad indentation!

if statement1:

    if statement2:

    print("both statement1 and statement2 are True")  # this line is not properly indented

[ ]

statement1 = False 

​

if statement1:

    print("printed if statement1 is True")

    

    print("still inside the if block")

[ ]

if statement1:

    print("printed if statement1 is True")

    

print("now outside the if block")

Loops

In Python, loops can be programmed in a number of different ways. The most common is the for loop, which is used together with iterable objects, such as lists. The basic syntax is:
for loops:
[ ]

for x in [1,2,3]:

    print(x)

The for loop iterates over the elements of the supplied list, and executes the containing block once for each element. Any kind of list can be used in the for loop. For example:
[ ]

for x in range(4): # by default range start at 0

    print(x)

Note: range(4) does not include 4 !
[ ]

for x in range(-3,3):

    print(x)

[ ]

for word in ["scientific", "computing", "with", "python"]:

    print(word)

To iterate over key-value pairs of a dictionary:
[ ]

for key, value in params.items():

    print(key + " = " + str(value))

Sometimes it is useful to have access to the indices of the values when iterating over a list. We can use the enumerate function for this:
[ ]

for idx, x in enumerate(range(-3,3)):

    print(idx, x)

List comprehensions: Creating lists using for loops:

A convenient and compact way to initialize lists:
[ ]

l1 = [x**2 for x in range(0,5)]

​

print(l1)

while loops:
[ ]

i = 0

​

while i < 5:

    print(i)

    

    i = i + 1

    

print("done")

Note that the print("done") statement is not part of the while loop body because of the difference in indentation.
Functions

A function in Python is defined using the keyword def, followed by a function name, a signature within parentheses (), and a colon :. The following code, with one additional level of indentation, is the function body.
[ ]

def func0():   

    print("test")

[ ]

func0()

Optionally, but highly recommended, we can define a so called "docstring", which is a description of the functions purpose and behaivor. The docstring should follow directly after the function definition, before the code in the function body.
[ ]

def func1(s):

    """

    Print a string 's' and tell how many characters it has    

    """

    

    print(s + " has " + str(len(s)) + " characters")

[ ]

help(func1)

[ ]

func1("test")

Functions that returns a value use the return keyword:
[ ]

def square(x):

    """

    Return the square of x.

    """

    return x ** 2

[ ]

square(4)

We can return multiple values from a function using tuples (see above):
[ ]

def powers(x):

    """

    Return a few powers of x.

    """

    return x ** 2, x ** 3, x ** 4

[ ]

powers(3)

[ ]

x2, x3, x4 = powers(3)

​

print(x3)

Default argument and keyword arguments

In a definition of a function, we can give default values to the arguments the function takes:
[ ]

def myfunc(x, p=2, debug=False):

    if debug:

        print("evaluating myfunc for x = " + str(x) + " using exponent p = " + str(p))

    return x**p

If we don't provide a value of the debug argument when calling the the function myfunc it defaults to the value provided in the function definition:
[ ]

myfunc(5)

[ ]

myfunc(5, debug=True)

If we explicitly list the name of the arguments in the function calls, they do not need to come in the same order as in the function definition. This is called keyword arguments, and is often very useful in functions that takes a lot of optional arguments.
[ ]

myfunc(p=3, debug=True, x=7)

Unnamed functions (lambda function)

In Python we can also create unnamed functions, using the lambda keyword:
[ ]

f1 = lambda x: x**2

    

# is equivalent to 

​

def f2(x):

    return x**2

[ ]

f1(2), f2(2)

This technique is useful for example when we want to pass a simple function as an argument to another function, like this:
[ ]

# map is a built-in python function

map(lambda x: x**2, range(-3,4))

[ ]

# in python 3 we can use `list(...)` to convert the iterator to an explicit list

list(map(lambda x: x**2, range(-3,4)))

Classes

Classes are the key features of object-oriented programming. A class is a structure for representing an object and the operations that can be performed on the object.

In Python a class can contain attributes (variables) and methods (functions).

A class is defined almost like a function, but using the class keyword, and the class definition usually contains a number of class method definitions (a function in a class).

    Each class method should have an argument self as its first argument. This object is a self-reference.

    Some class method names have special meaning, for example:
        __init__: The name of the method that is invoked when the object is first created.
        __str__ : A method that is invoked when a simple string representation of the class is needed, as for example when printed.
        There are many more, see http://docs.python.org/2/reference/datamodel.html#special-method-names

[ ]

class Point:

    """

    Simple class for representing a point in a Cartesian coordinate system.

    """

    

    def __init__(self, x, y):

        """

        Create a new Point at x, y.

        """

        self.x = x

        self.y = y

        

    def translate(self, dx, dy):

        """

        Translate the point by dx and dy in the x and y direction.

        """

        self.x += dx

        self.y += dy

        

    def __str__(self):

        return("Point at [%f, %f]" % (self.x, self.y))

To create a new instance of a class:
[ ]

p1 = Point(0, 0) # this will invoke the __init__ method in the Point class

​

print(p1)         # this will invoke the __str__ method

To invoke a class method in the class instance p:
[ ]

p2 = Point(1, 1)

​

p1.translate(0.25, 1.5)

​

print(p1)

print(p2)

Note that calling class methods can modifiy the state of that particular class instance, but does not effect other class instances or any global variables.

That is one of the nice things about object-oriented design: code such as functions and related variables are grouped in separate and independent entities.
Modules

One of the most important concepts in good programming is to reuse code and avoid repetitions.

The idea is to write functions and classes with a well-defined purpose and scope, and reuse these instead of repeating similar code in different part of a program (modular programming). The result is usually that readability and maintainability of a program is greatly improved. What this means in practice is that our programs have fewer bugs, are easier to extend and debug/troubleshoot.

Python supports modular programming at different levels. Functions and classes are examples of tools for low-level modular programming. Python modules are a higher-level modular programming construct, where we can collect related variables, functions and classes in a module. A python module is defined in a python file (with file-ending .py), and it can be made accessible to other Python modules and programs using the import statement.

Consider the following example: the file mymodule.py contains simple example implementations of a variable, function and a class:
[ ]

%%file mymodule.py

"""

Example of a python module. Contains a variable called my_variable,

a function called my_function, and a class called MyClass.

"""

​

my_variable = 0

​

def my_function():

    """

    Example function

    """

    return my_variable

    

class MyClass:

    """

    Example class.

    """

​

    def __init__(self):

        self.variable = my_variable

        

    def set_variable(self, new_value):

        """

        Set self.variable to a new value

        """

        self.variable = new_value

        

    def get_variable(self):

        return self.variable

We can import the module mymodule into our Python program using import:
[ ]

import mymodule

Use help(module) to get a summary of what the module provides:
[ ]

help(mymodule)

[ ]

mymodule.my_variable

[ ]

mymodule.my_function() 

[ ]

my_class = mymodule.MyClass() 

my_class.set_variable(10)

my_class.get_variable()

If we make changes to the code in mymodule.py, we need to reload it using reload:
[ ]

reload(mymodule)  # works only in python 2

Exceptions

In Python errors are managed with a special language construct called "Exceptions". When errors occur exceptions can be raised, which interrupts the normal program flow and fallback to somewhere else in the code where the closest try-except statement is defined.

To generate an exception we can use the raise statement, which takes an argument that must be an instance of the class BaseException or a class derived from it.
[ ]

raise Exception("description of the error")

A typical use of exceptions is to abort functions when some error condition occurs, for example:

def my_function(arguments):

    if not verify(arguments):
        raise Exception("Invalid arguments")

    # rest of the code goes here

To gracefully catch errors that are generated by functions and class methods, or by the Python interpreter itself, use the try and except statements:

try:
    # normal code goes here
except:
    # code for error handling goes here
    # this code is not executed unless the code
    # above generated an error

For example:
[ ]

try:

    print("test")

    # generate an error: the variable test is not defined

    print(test)

except:

    print("Caught an exception")

To get information about the error, we can access the Exception class instance that describes the exception by using for example:

except Exception as e:

[ ]

try:

    print("test")

    # generate an error: the variable test is not defined

    print(test)

except Exception as e:

    print("Caught an exception:" + str(e))

Further reading

    http://www.python.org - The official web page of the Python programming language.
    http://www.python.org/dev/peps/pep-0008 - Style guide for Python programming. Highly recommended.
    http://www.greenteapress.com/thinkpython/ - A free book on Python programming.
    Python Essential Reference - A good reference book on Python programming.

