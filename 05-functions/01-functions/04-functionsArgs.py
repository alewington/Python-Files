# Function Arguements

# Arguements are the values that you pass to a function when it is called.
# The arguements can be any data type, but they must always be passed in order.

def my_function(x: int, y: int) -> int:
    """Addition of two numbers
    Args:
        x (int): number (parameter) to be added
        y (int): number (parameter) to be added
    Returns:
        int: Sum of x and y
    Example:
        >>> my_function(5, 6)
        11
    """
    return x + y


result: int = my_function(5, 6)
print(result)
# The first arguement is: 5
# The second arguement is: 6

# The first parameter is x and gets 5
# The second parameter is y and gets 6

# These are arguements because 5 and 6 are passed to the function.

# The difference between a parameter and arguement is that parameters are
# defined in the function definition, but arguements are passed when you call
# the function.
