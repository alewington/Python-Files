# enums

# Enums are a way to define a set of named values. They can be used to
# represent a collection of related constants, making code more readable
# and maintainable.
# Enums are defined using the enum module.

from enum import Enum


class colour(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# Example usage of the colour enum
def print_colour(colour):
    """Prints the name of the colour.
  Args:
        colour (colour): An instance of the colour enum.
    Returns:
        None
    Raises:
        None
    Example:
        >>> print_colour(colour.RED)
        The colour is Red.
    """
    if colour == colour.RED:
        print("The colour is Red.")
    elif colour == colour.GREEN:
        print("The colour is Green.")
    elif colour == colour.BLUE:
        print("The colour is Blue.")
    else:
        print("Unknown colour.")


# Testing the print_colour function with different enum values
print_colour(colour.RED)    # Output: The colour is Red.
print_colour(colour.GREEN)  # Output: The colour is Green.

# Testing the print_colour function with an unknown colour
# print_colour(4)  # Output: Unknown colour.

# Accessing enum members and their values
print(colour.RED)          # Output: colour.RED
print(colour.RED.name)     # Output: RED
print(colour.RED.value)    # Output: 1

# Iterating over enum members
for colour in colour:
    print(f"{colour.name} = {colour.value}")

# Comparing enum members
print(colour.RED == colour.GREEN)  # Output: False
print(colour.RED == colour.RED)    # Output: True

# enums can also be used in switch-like statements using if-elif-else
# constructs, as shown in the print_colour function. They provide a clear
# and structured way to handle a set of related constants, improving code
# clarity and reducing the likelihood of errors.
