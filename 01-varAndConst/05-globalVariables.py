# Global Variables

# Global variables are variables that are defined outside of any function and
# can be accessed from anywhere in the code.
# <-- here we define a global variable
global_variable = "I am a global variable"


def my_function():
    # <-- we can access the global variable inside the function
    print(global_variable)


my_function()  # Output: I am a global

# #############################################################
# creating local variable inside a function and trying to access it
# outside the function


def my_function_with_local_variable():
    local_variable = "I am a local variable"
    print(local_variable)  # Output: I am a local variable
    return local_variable


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
