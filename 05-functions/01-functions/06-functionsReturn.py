# Return in Functions

# Return in Functions is used to return a value from a function.
# The return statement accepts an expression as its argument, and returns the
# value of that expression.
# If no argument is passed, None is returned.
c: list[int] = []


def choose() -> int:
    """Chooses a number from user input. The user must enter an integer.
        Args:
            None
        Returns:
            int: The integer entered by the user
        Example:
            >>> choose()
            5
    """
    i: int = int(input("Choose a number to add:"))
    return i


def numbers_to_add() -> list[int]:
    """ Adds two numbers from user input of Choose()
    Args:
        None
    Returns:
        list[int]: The list of numbers entered by the user
    Example:
        >>> numbers_to_add()
        [5, 7]
    """
    for p in range(2):
        c.append(choose())
    return c


def layout() -> str:
    """ Adds two numbers from user input of Choose()
    Args:
        None
    Returns:
        str: _description_
    Example:
        >>> layout()
        The sum of 5 and 7 is 12.
    """
    numbers_to_add()
    return f"The sum of {c[0]} and {c[1]} is {sum(c)}."


print(layout())

# Output:
# Choose a number to add:5
# Choose a number to add:7
# The sum of 5 and 7 is 12.

# The return statement can be used in any function, even the main program.
# If it is not used, None is returned by default.
