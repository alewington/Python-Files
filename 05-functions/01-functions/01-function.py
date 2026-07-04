# Functions

# Finally Functions.
# Functions are 1st class objects in Python.
# They can be passed around like any other object.
# They can be assigned to variables, stored in data structures, etc.
# You can even return a function from another function!

# What do they do
# They allow you to group code together and reuse it.
# You can think of functions as subroutines in other languages.
# Functions can be defined anywhere in your code, but they must be defined
# before you use them.
# You can also define functions inside other functions.
# Functions can be defined in modules, classes, or anywhere else that you
# can put code.

# Definition of a function:
# 1. The def keyword is used to define a new function.
# 2. The name of the function follows the def keyword.
# 3. Parentheses follow the function name. These are called parameters.
#    They are data passed into the function.
# 4. A colon at the end of the line indicates the start of the code block.
# 5. The code to be executed is indented, and ends in a new line.
# 6. The return keyword is used to send data back from the function.
#    If not specified, None is returned implicitly.


def say_hello():
    """ This is a docstring.
    It can be accessed using the __doc__ attribute of the function object.
        Args:
            None
        Returns:
            A string
        Example:
            >>> print(say_hello.__doc__)
            This is a docstring.
    """

    return "Hello"


# Calling a function:
# 1. The name of the function is used to call it.
# 2. Parentheses follow the function name. These are called arguments.
#    They are data passed into the function.
# 3. A new line indicates the end of the code block.

print(say_hello())  # Hello
