# Recursion

# Recursion is a technique in which a function calls itself.
# This can be used to solve problems that are naturally recursive, such as
# traversing a tree or searching for an item in a list.

# Advantages:
# - Easy to understand
# - Easy to write
# - Easy to debug
# - Can be used to solve problems that are naturally recursive
# Disadvantages:
# - Not as efficient as iterative solutions
# - Can cause stack overflows if not written correctly
# - Harder to read and maintain than iterative solutions
# - more processor intensive

# 1. Factorial
def fibonacci(n):
    """return true or false or a value
    Args:
        n (int): an integer value
    Returns:
        int: 0, 1, 2, 3, 5
    Example:
        >>> fibonacci(5)
        0,1,1,2,3,5

    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


for i in range(10):
    print(fibonacci(i))
