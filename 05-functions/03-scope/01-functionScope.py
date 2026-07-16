# Scope

# Scope is the set of names that are available in a particular piece of code.
# A name can be a variable, function or class name.

# Global scope
# The global scope is the set of all names that are defined at the top level
# of your program.
# These names are always available to any other part of your program.

# Local scope
# The local scope is the set of names that are defined inside a function,
# class or loop.
# These names are only available within that particular piece of code.

# Global and local scope in Python
# In Python, global and local scope are determined by where you define your
# variables.
# If you define a variable outside of any functions, it is a global variable.
# If you define a variable inside a function, it is a local variable.

# Example:
x = 5  # x is a global variable


def my_function():
    """ print values from global and local
    Args:
        None
    Returns:
        None
    Example:
        >>> my_function()
        10
    """
    global z
    y = 10  # y is a local variable
    print(y)
    z = 3  # defines the global z to 3
    print(z)  # prints 3
    print(x)  # prints 5


my_function()
print(x)
print(z)
