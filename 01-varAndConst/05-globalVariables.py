# Global Variables

# Global variables are variables that are defined outside of any function and
# can be accessed from anywhere in the code.
# <-- here we define a global variable
global_variable = "I am a global variable"


def my_function():
    # <-- we can access the global variable inside the function
    print(global_variable)
    """ Note: The global variable 'global_variable' can be accessed inside the
    function 'my_function' because it is defined in the global scope. However,
    if you try to modify the global variable inside the function without
    declaring it as global, it will create a new local variable with
    the same name, and the global variable will remain unchanged.
    Args: None

    Returns: None
    """


my_function()  # Output: I am a global

# #############################################################
# creating local variable inside a function and trying to access it
# outside the function


def my_function_with_local_variable():
    local_variable = "I am a local variable"
    print(local_variable)  # Output: I am a local variable
    return local_variable
    """ Note: The local variable 'local_variable' is only accessible within
    the function'my_function_with_local_variable'. It cannot be accessed
    outside of the function, but we can return it from the function
    and assign it to a global variable if needed.

    Args: None

    Returns: local_variable (str): The local variable that was created
    inside the function
    """


calling_local = my_function_with_local_variable()
print(calling_local)  # Output: I am a local variable, still the same one but
# was returned to the global scope
print(global_variable)  # Output: I am a global variable

# ###############################################################
# Modifiying globals in functions
# If we try to modify a global variable inside a function without declaring it
# as global, it will create a new local variable with the same name, and the
# global variable will remain unchanged.

# We can also modify a global variable inside a function using
# the 'global' keyword.


def modify_global_variable():
    global global_variable
# <-- we need to declare the variable as global to modify it in a function
    global_variable = "I have been modified"


modify_global_variable()


print(global_variable)  # Output: I have been modified
